"""
Smart Kitchen Recipe Finder - Console Application
A CLI application for discovering 5-ingredient recipes based on available pantry items,
complete with fuzzy ingredient matching, step-by-step instructions, and a smart grocery cart.
"""
#Terminal logic

import os    #Import os module
import sys   #for standard I/O streams
import json  #for reading data
import difflib #for sequence matching

# Attempt to import fuzzy matching library; fallback to standard library difflib
try:
    from thefuzz import fuzz
    HAS_THEFUZZ = True       #fuzzy logic means match uppercase and lowercase letters
except ImportError:
    HAS_THEFUZZ = False

# Ensure robust UTF-8 encoding across Windows cmd/powershell/terminals
try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")       #standard I/O, errors streams
    if hasattr(sys.stdin, "reconfigure"):                                #Ensure emojis and special character render
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# Enable ANSI colors on Windows terminals
if sys.platform == "win32":
    os.system("")

# -----------------------------------------------------------------------------
# ANSI Color Codes & Formatting
# -----------------------------------------------------------------------------
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"         
    GREEN = "\033[92m"
    YELLOW = "\033[93m"       #color codes
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    DIM = "\033[2m"
    RESET = "\033[0m"

def print_banner():  #Helper function
    banner = f"""{Colors.CYAN}{Colors.BOLD}
================================================================================
   🍳  SMART KITCHEN RECIPE FINDER  🍳
   Turn Your Pantry Ingredients Into Delicious Chef-Crafted Meals!
================================================================================{Colors.RESET}"""
    print(banner)

def print_header(title):  #Helper function
    print(f"\n{Colors.BOLD}{Colors.CYAN}--- {title} ---{Colors.RESET}")

def print_divider():     #Helper functions
    print(f"{Colors.DIM}--------------------------------------------------------------------------------{Colors.RESET}")







#Data base


# -----------------------------------------------------------------------------
# Recipe Database & Search Engine
# -----------------------------------------------------------------------------
class RecipeDatabase:
    def __init__(self, json_path=None):
        if json_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(base_dir, "recipes.json")
        self.json_path = json_path
        self.recipes = []
        self.load_data()
                                     #Loads the recipes.json file
    def load_data(self):
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                self.recipes = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.recipes = []       #if file not found it defaults to an empty list

    def get_stats(self):
        breakfast = sum(1 for r in self.recipes if r.get("meal_type") == "Breakfast")
        lunch = sum(1 for r in self.recipes if r.get("meal_type") == "Lunch")
        dinner = sum(1 for r in self.recipes if r.get("meal_type") == "Dinner")
        ingredients = set()
        for r in self.recipes:
            for ing in r.get("ingredients", []):
                ingredients.add(ing.strip().lower())    #Keep record
        return {
            "total": len(self.recipes),
            "breakfast": breakfast,
            "lunch": lunch,
            "dinner": dinner,
            "unique_ingredients": len(ingredients),
            "ingredients_list": sorted(list(ingredients))
        }

    @staticmethod
    def _match_single_word(u_word, r_word, threshold=80):
        u = u_word.strip().lower()
        r = r_word.strip().lower()
        if not u or not r:
            return False

        # Exact match
        if u == r:
            return True

        # Common plural / singular transformations
        if u + "s" == r or r + "s" == u:
            return True
        if u + "es" == r or r + "es" == u:
            return True
        if u.endswith("ies") and u[:-3] + "y" == r:
            return True
        if r.endswith("ies") and r[:-3] + "y" == u:
            return True

        # Fuzzy string similarity
        if HAS_THEFUZZ:
            score = max(fuzz.ratio(u, r), fuzz.token_sort_ratio(u, r))
        else:
            score = int(difflib.SequenceMatcher(None, u, r).ratio() * 100)

        min_len = min(len(u), len(r))
        if min_len <= 3:
            return score == 100
        elif min_len <= 4:
            return score >= 88
        return score >= threshold

    @classmethod
    def ingredient_matches(cls, user_ing, recipe_ing, threshold=80):
        u = user_ing.strip().lower()
        r = recipe_ing.strip().lower()
        if not u or not r:
            return False          

        if cls._match_single_word(u, r, threshold):
            return True
                               #Handles multi-word ingredient phrases (e.g., matching "cheddar cheese"
                               # Multi-word matching (e.g. 'cheddar cheese' matched by 'cheese' or 'cheddar')
        u_words = u.split()
        r_words = r.split()
        if len(u_words) > 1 or len(r_words) > 1:
            for uw in u_words:
                if len(uw) >= 4 and any(cls._match_single_word(uw, rw, threshold) for rw in r_words):
                    return True
            for rw in r_words:
                if len(rw) >= 4 and any(cls._match_single_word(rw, uw, threshold) for uw in u_words):
                    return True
        return False

    def search(self, user_ingredients_list, min_matches=4, meal_filter="All"):
        user_ings = [i.strip().lower() for i in user_ingredients_list if i.strip()]
        if not user_ings:
            return []
                                 #Filters recipes based on selected meal categories
        matched_recipes = []
        for recipe in self.recipes:
            if meal_filter != "All" and recipe.get("meal_type", "").lower() != meal_filter.lower():
                continue

            recipe_ings = recipe.get("ingredients", [])
            matched = []
            for r_ing in recipe_ings:
                for u_ing in user_ings:
                    if self.ingredient_matches(u_ing, r_ing):
                        matched.append(r_ing)
                        break

            match_count = len(matched)
            if match_count >= min_matches and match_count <= len(recipe_ings):
                missing = [ing for ing in recipe_ings if ing not in matched]
                matched_recipes.append({
                    "title": recipe["title"],
                    "meal_type": recipe.get("meal_type", "Recipe"),
                    "matched_ingredients": matched,
                    "missing_ingredients": missing,
                    "match_count": match_count,
                    "total_required": recipe_ings,
                    "steps": recipe.get("steps", []),
                    "youtube_url": recipe.get("youtube_url", "")
                })

        # Rank with highest match count first
        matched_recipes.sort(key=lambda r: r["match_count"], reverse=True)
        return matched_recipes















# -----------------------------------------------------------------------------
# Smart Grocery Cart
# -----------------------------------------------------------------------------
class GroceryCart:
    def __init__(self):      #Adds items to the cart
        self.items = []

    def add(self, item_name, recipe_title=None):
        clean = item_name.strip()
        if not clean:
            return
        for item in self.items:
            if item["name"].lower() == clean.lower():
                item["quantity"] += 1
                if recipe_title and recipe_title not in item["recipes"]:
                    item["recipes"].append(recipe_title)
                return
        self.items.append({        
            "name": clean,
            "quantity": 1,
            "recipes": [recipe_title] if recipe_title else []
        })

    def add_multiple(self, item_list, recipe_title=None):
        for item in item_list:
            self.add(item, recipe_title)

    def remove(self, index):       #Allow users to delete individual items
        if 0 <= index < len(self.items):
            removed = self.items.pop(index)
            return removed
        return None

    def clear(self):
        self.items.clear()

    def total_count(self):   #returns the total no of items present in cart
        return sum(item["quantity"] for item in self.items)

    def export_to_text(self, filepath="smart_grocery_list.txt"):   #
        lines = ["🛒 Smart Kitchen Grocery List:", "=" * 35]
        for item in self.items:
            recipes_info = f" (For: {', '.join(item['recipes'])})" if item["recipes"] else ""
            lines.append(f"• {item['name'].title()} (Qty: {item['quantity']}){recipes_info}")
        content = "\n".join(lines)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath

# -----------------------------------------------------------------------------
# Interactive Console Application
# -----------------------------------------------------------------------------
class SmartRecipeApp:
    PRESETS = [
        ("Breakfast Eggs & Toast", "bread, eggs, cheese, butter, spinach"),
        ("Italian Night", "pasta, tomato, garlic, olive oil, basil"),
        ("Crispy Hash Browns", "potato, onions, butter, olive oil, paprika"),
        ("Quick Stir Fry", "rice, soy sauce, carrots, peppers, oil"),
        ("Salmon Feast", "salmon, lemon, garlic, butter, parsley")
    ]

    def __init__(self):
        self.db = RecipeDatabase()
        self.cart = GroceryCart()

    def run(self):
        print_banner()
        while True:
            self.show_main_menu()
            choice = input(f"\n{Colors.BOLD}Select an option (1-6): {Colors.RESET}").strip()
            if choice == "1":
                self.search_by_ingredients_menu()
            elif choice == "2":
                self.pantry_presets_menu()
            elif choice == "3":
                self.browse_recipes_menu()
            elif choice == "4":
                self.grocery_cart_menu()
            elif choice == "5":
                self.database_stats_menu()
            elif choice in ("6", "q", "quit", "exit"):
                print(f"\n{Colors.GREEN}Thank you for using Smart Kitchen Recipe Finder! Happy cooking! 🍽️{Colors.RESET}\n")
                break
            else:
                print(f"{Colors.RED}Invalid option. Please choose between 1 and 6.{Colors.RESET}")

    def show_main_menu(self):
        cart_badge = f" ({self.cart.total_count()} items)" if self.cart.total_count() > 0 else ""
        print(f"\n{Colors.BOLD}{Colors.YELLOW}MAIN MENU:{Colors.RESET}")
        print(f"  {Colors.BOLD}[1]{Colors.RESET} 🔍 Search Recipes by Ingredients")
        print(f"  {Colors.BOLD}[2]{Colors.RESET} 💡 Quick Pantry Presets")
        print(f"  {Colors.BOLD}[3]{Colors.RESET} 📖 Browse All Recipes")
        print(f"  {Colors.BOLD}[4]{Colors.RESET} 🛒 View & Manage Grocery Cart{Colors.GREEN}{cart_badge}{Colors.RESET}")
        print(f"  {Colors.BOLD}[5]{Colors.RESET} 📊 Kitchen Database & Ingredients Stats")
        print(f"  {Colors.BOLD}[6]{Colors.RESET} ❌ Exit")

    # -------------------------------------------------------------------------
    # Option 1: Search by Ingredients
    # -------------------------------------------------------------------------
    def search_by_ingredients_menu(self, prefilled_ingredients=None):
        print_header("Search Recipes by Pantry Ingredients")
        if prefilled_ingredients:
            raw_input = prefilled_ingredients
            print(f"{Colors.BOLD}Using ingredients:{Colors.RESET} {Colors.GREEN}{raw_input}{Colors.RESET}")
        else:
            print("Enter ingredients available in your pantry, separated by commas.")
            print(f"{Colors.DIM}Example: tomato, potato, eggs, cheese, butter, garlic{Colors.RESET}")
            raw_input = input(f"{Colors.BOLD}Pantry ingredients: {Colors.RESET}").strip()

        if not raw_input:
            print(f"{Colors.RED}No ingredients entered. Returning to menu.{Colors.RESET}")
            return

        user_ingredients = [x.strip() for x in raw_input.split(",") if x.strip()]

        # Meal Category filter
        print("\nFilter by Meal Category:")
        print("  1: All Meals (Default)")
        print("  2: Breakfast")
        print("  3: Lunch")
        print("  4: Dinner")
        meal_choice = input(f"{Colors.BOLD}Choice (1-4, Enter for All): {Colors.RESET}").strip()
        meal_filter = "All"
        if meal_choice == "2":
            meal_filter = "Breakfast"
        elif meal_choice == "3":
            meal_filter = "Lunch"
        elif meal_choice == "4":
            meal_filter = "Dinner"

        # Minimum match threshold
        print(f"\nMinimum ingredient match requirement (each recipe uses 5 ingredients):")
        print("  4: At least 4 of 5 ingredients matched (Recommended)")
        print("  5: Exact 5/5 full match only")
        print("  3: 3 or more matched (broader search)")
        thresh_input = input(f"{Colors.BOLD}Minimum matches (3-5, Default 4): {Colors.RESET}").strip()
        min_matches = 4
        if thresh_input in ("3", "4", "5"):
            min_matches = int(thresh_input)

        results = self.db.search(user_ingredients, min_matches=min_matches, meal_filter=meal_filter)
        self.display_search_results(results, user_ingredients, min_matches, meal_filter)

    # -------------------------------------------------------------------------
    # Display Search Results & Recipe Selection
    # -------------------------------------------------------------------------
    def display_search_results(self, results, user_ingredients, min_matches, meal_filter):
        category_str = f" for '{meal_filter}'" if meal_filter != "All" else ""
        if not results:
            print(f"\n{Colors.YELLOW}No recipes found matching at least {min_matches} of your ingredients{category_str}.{Colors.RESET}")
            print(f"Tip: Try adding common kitchen staples (butter, garlic, oil, eggs, bread) or lower the match threshold.")
            input(f"\n{Colors.DIM}Press Enter to return to main menu...{Colors.RESET}")
            return

        while True:
            print_header(f"Found {len(results)} Matching Recipe(s){category_str}")
            print(f"{Colors.DIM}Ranked from highest match to lowest:{Colors.RESET}\n")

            for idx, r in enumerate(results, 1):
                match_str = f"{r['match_count']}/5 Matched"
                if r['match_count'] == 5:
                    match_badge = f"{Colors.GREEN}{Colors.BOLD}★ {match_str} (FULL PANTRY MATCH!){Colors.RESET}"
                else:
                    match_badge = f"{Colors.YELLOW}{Colors.BOLD}● {match_str}{Colors.RESET}"

                meal_badge = f"{Colors.CYAN}[{r['meal_type']}]{Colors.RESET}"
                print(f"  {Colors.BOLD}[{idx}] {r['title']}{Colors.RESET}  {meal_badge}  {match_badge}")

                matched_list = ", ".join(r['matched_ingredients'])
                print(f"      {Colors.GREEN}✓ Matched:{Colors.RESET} {matched_list}")

                if r['missing_ingredients']:
                    missing_list = ", ".join(r['missing_ingredients'])
                    print(f"      {Colors.RED}✗ Missing:{Colors.RESET} {missing_list}")
                else:
                    print(f"      {Colors.GREEN}✓ Missing:{Colors.RESET} None - You have everything!")
                print()

            print_divider()
            print(f"Actions:")
            print(f"  • Enter {Colors.BOLD}[1-{len(results)}]{Colors.RESET} to view cooking steps & details")
            print(f"  • Enter {Colors.BOLD}a <number>{Colors.RESET} (e.g. 'a 2') to add missing items to your Cart")
            print(f"  • Enter {Colors.BOLD}b{Colors.RESET} to go back to main menu")

            sub_choice = input(f"\n{Colors.BOLD}Selection: {Colors.RESET}").strip().lower()
            if sub_choice == "b" or sub_choice == "":
                break

            if sub_choice.startswith("a "):
                parts = sub_choice.split()
                if len(parts) == 2 and parts[1].isdigit():
                    num = int(parts[1])
                    if 1 <= num <= len(results):
                        rec = results[num - 1]
                        if rec["missing_ingredients"]:
                            self.cart.add_multiple(rec["missing_ingredients"], rec["title"])
                            print(f"{Colors.GREEN}Added {len(rec['missing_ingredients'])} missing item(s) to your Grocery Cart! 🛒{Colors.RESET}")
                        else:
                            print(f"{Colors.YELLOW}No missing ingredients for this recipe! You're ready to cook! 🎉{Colors.RESET}")
                    else:
                        print(f"{Colors.RED}Invalid recipe number.{Colors.RESET}")
                else:
                    print(f"{Colors.RED}Use format 'a 1' to add missing items for recipe 1.{Colors.RESET}")
                continue

            if sub_choice.isdigit():
                num = int(sub_choice)
                if 1 <= num <= len(results):
                    self.show_recipe_details(results[num - 1])
                else:
                    print(f"{Colors.RED}Invalid number. Please select between 1 and {len(results)}.{Colors.RESET}")
            else:
                print(f"{Colors.RED}Unrecognized choice. Type a recipe number, 'a <num>', or 'b'.{Colors.RESET}")

    # -------------------------------------------------------------------------
    # Recipe Detailed View
    # -------------------------------------------------------------------------
    def show_recipe_details(self, recipe):
        print("\n" + "=" * 80)
        print(f"  {Colors.BOLD}{Colors.CYAN}🍲 {recipe['title'].upper()}{Colors.RESET} ({recipe['meal_type']})")
        print("=" * 80)

        # Ingredients section
        print(f"\n{Colors.BOLD}Ingredients (5 Required):{Colors.RESET}")
        for ing in recipe.get("total_required", recipe.get("ingredients", [])):
            if "matched_ingredients" in recipe:
                if ing in recipe["matched_ingredients"]:
                    print(f"  {Colors.GREEN}[✓ In Pantry] {ing}{Colors.RESET}")
                else:
                    print(f"  {Colors.RED}[✗ Missing  ] {ing}{Colors.RESET}")
            else:
                print(f"  • {ing}")

        # Cooking instructions
        print(f"\n{Colors.BOLD}Step-by-Step Cooking Instructions:{Colors.RESET}")
        steps = recipe.get("steps", [])
        if steps:
            for i, step in enumerate(steps, 1):
                print(f"  {Colors.BOLD}{i}.{Colors.RESET} {step}")
        else:
            print("  No instructions recorded.")

        # Video tutorial link
        yt_url = recipe.get("youtube_url")
        if yt_url:
            print(f"\n{Colors.BOLD}🎬 Video Tutorial:{Colors.RESET} {Colors.BLUE}{yt_url}{Colors.RESET}")

        print("\n" + "-" * 80)
        missing = recipe.get("missing_ingredients", [])
        if missing:
            print(f"Enter {Colors.BOLD}'a'{Colors.RESET} to add missing ingredients ({', '.join(missing)}) to Cart")
        print(f"Press {Colors.BOLD}Enter{Colors.RESET} to return to recipes list")

        action = input(f"{Colors.BOLD}Action: {Colors.RESET}").strip().lower()
        if action == "a" and missing:
            self.cart.add_multiple(missing, recipe["title"])
            print(f"{Colors.GREEN}Added {len(missing)} item(s) to your Grocery Cart! 🛒{Colors.RESET}")

    # -------------------------------------------------------------------------
    # Option 2: Quick Pantry Presets
    # -------------------------------------------------------------------------
    def pantry_presets_menu(self):
        print_header("Quick Pantry Presets")
        print("Select a pre-configured pantry basket to find recipes instantly:")
        for idx, (name, ings) in enumerate(self.PRESETS, 1):
            print(f"  {Colors.BOLD}[{idx}]{Colors.RESET} {Colors.CYAN}{name}{Colors.RESET}")
            print(f"      {Colors.DIM}{ings}{Colors.RESET}")

        print(f"  {Colors.BOLD}[b]{Colors.RESET} Back to Main Menu")
        choice = input(f"\n{Colors.BOLD}Select preset (1-{len(self.PRESETS)}): {Colors.RESET}").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(self.PRESETS):
                _, selected_ings = self.PRESETS[idx - 1]
                self.search_by_ingredients_menu(prefilled_ingredients=selected_ings)
            else:
                print(f"{Colors.RED}Invalid preset number.{Colors.RESET}")

    # -------------------------------------------------------------------------
    # Option 3: Browse All Recipes
    # -------------------------------------------------------------------------
    def browse_recipes_menu(self):
        print_header("Browse All Indexed Recipes")
        print("Choose a category to browse:")
        print("  1: All Recipes")
        print("  2: Breakfast")
        print("  3: Lunch")
        print("  4: Dinner")
        print("  b: Back to Main Menu")
        c = input(f"{Colors.BOLD}Category (1-4): {Colors.RESET}").strip().lower()
        if c == "b":
            return

        category = "All"
        if c == "2":
            category = "Breakfast"
        elif c == "3":
            category = "Lunch"
        elif c == "4":
            category = "Dinner"

        filtered = [
            r for r in self.db.recipes
            if category == "All" or r.get("meal_type", "").lower() == category.lower()
        ]

        if not filtered:
            print(f"{Colors.YELLOW}No recipes found in this category.{Colors.RESET}")
            return

        while True:
            print_header(f"Recipes in '{category}' ({len(filtered)} items)")
            for idx, r in enumerate(filtered, 1):
                ings_summary = ", ".join(r.get("ingredients", []))
                print(f"  {Colors.BOLD}[{idx:2d}] {r['title']}{Colors.RESET} {Colors.CYAN}[{r.get('meal_type')}]{Colors.RESET}")
                print(f"       {Colors.DIM}Ingredients: {ings_summary}{Colors.RESET}")

            print_divider()
            print(f"Enter {Colors.BOLD}[1-{len(filtered)}]{Colors.RESET} to view recipe details, or {Colors.BOLD}b{Colors.RESET} to return.")
            sel = input(f"{Colors.BOLD}Selection: {Colors.RESET}").strip().lower()
            if sel in ("b", ""):
                break
            if sel.isdigit():
                num = int(sel)
                if 1 <= num <= len(filtered):
                    rec = filtered[num - 1]
                    # Structure recipe dictionary for viewer
                    viewer_rec = {
                        "title": rec["title"],
                        "meal_type": rec.get("meal_type", "Recipe"),
                        "ingredients": rec.get("ingredients", []),
                        "total_required": rec.get("ingredients", []),
                        "steps": rec.get("steps", []),
                        "youtube_url": rec.get("youtube_url", "")
                    }
                    self.show_recipe_details(viewer_rec)
                else:
                    print(f"{Colors.RED}Invalid selection.{Colors.RESET}")

    # -------------------------------------------------------------------------
    # Option 4: Smart Grocery Cart
    # -------------------------------------------------------------------------
    def grocery_cart_menu(self):
        while True:
            print_header(f"🛒 Smart Grocery Cart ({self.cart.total_count()} items)")
            if not self.cart.items:
                print(f"{Colors.YELLOW}Your grocery cart is currently empty.{Colors.RESET}")
                print("Missing ingredients from recipe searches can be added here with one click!")
            else:
                for idx, item in enumerate(self.cart.items, 1):
                    rec_tag = f" {Colors.DIM}(For: {', '.join(item['recipes'])}){Colors.RESET}" if item["recipes"] else ""
                    print(f"  {Colors.BOLD}[{idx}]{Colors.RESET} {item['name'].title()} {Colors.CYAN}(Qty: {item['quantity']}){Colors.RESET}{rec_tag}")

            print_divider()
            print("Cart Options:")
            print(f"  {Colors.BOLD}[a]{Colors.RESET} Add custom ingredient")
            print(f"  {Colors.BOLD}[r]{Colors.RESET} Remove an item by number")
            print(f"  {Colors.BOLD}[c]{Colors.RESET} Clear entire cart")
            print(f"  {Colors.BOLD}[s]{Colors.RESET} Save / Export shopping list to file")
            print(f"  {Colors.BOLD}[b]{Colors.RESET} Back to Main Menu")

            cmd = input(f"\n{Colors.BOLD}Cart Action: {Colors.RESET}").strip().lower()
            if cmd in ("b", ""):
                break
            elif cmd == "a":
                new_item = input(f"{Colors.BOLD}Enter ingredient name to add: {Colors.RESET}").strip()
                if new_item:
                    self.cart.add(new_item)
                    print(f"{Colors.GREEN}Added '{new_item}' to cart!{Colors.RESET}")
            elif cmd == "r":
                if not self.cart.items:
                    print(f"{Colors.RED}Cart is already empty.{Colors.RESET}")
                    continue
                num_str = input(f"{Colors.BOLD}Enter item number to remove (1-{len(self.cart.items)}): {Colors.RESET}").strip()
                if num_str.isdigit():
                    idx = int(num_str) - 1
                    removed = self.cart.remove(idx)
                    if removed:
                        print(f"{Colors.GREEN}Removed '{removed['name']}' from cart.{Colors.RESET}")
                    else:
                        print(f"{Colors.RED}Invalid item number.{Colors.RESET}")
            elif cmd == "c":
                confirm = input(f"{Colors.YELLOW}Are you sure you want to clear your cart? (y/n): {Colors.RESET}").strip().lower()
                if confirm == "y":
                    self.cart.clear()
                    print(f"{Colors.GREEN}Grocery cart cleared.{Colors.RESET}")
            elif cmd == "s":
                if not self.cart.items:
                    print(f"{Colors.RED}Cart is empty. Nothing to export.{Colors.RESET}")
                    continue
                filename = self.cart.export_to_text()
                print(f"{Colors.GREEN}Successfully saved shopping list to '{filename}'! 📝{Colors.RESET}")

    # -------------------------------------------------------------------------
    # Option 5: Database Statistics
    # -------------------------------------------------------------------------
    def database_stats_menu(self):
        stats = self.db.get_stats()
        print_header("Kitchen Database Statistics")
        print(f"  • {Colors.BOLD}Total Recipes Indexed:{Colors.RESET} {Colors.GREEN}{stats['total']}{Colors.RESET}")
        print(f"  • {Colors.BOLD}Breakfast Recipes:{Colors.RESET}     {stats['breakfast']}")
        print(f"  • {Colors.BOLD}Lunch Recipes:{Colors.RESET}         {stats['lunch']}")
        print(f"  • {Colors.BOLD}Dinner Recipes:{Colors.RESET}        {stats['dinner']}")
        print(f"  • {Colors.BOLD}Unique Ingredients:{Colors.RESET}    {Colors.CYAN}{stats['unique_ingredients']}{Colors.RESET}")

        print_divider()
        view_ings = input(f"Would you like to list all {stats['unique_ingredients']} available ingredients? (y/n): ").strip().lower()
        if view_ings == "y":
            print(f"\n{Colors.BOLD}Available Ingredients in Database:{Colors.RESET}")
            ings = stats['ingredients_list']
            # Format nicely in 3 columns
            col_width = 25
            for i in range(0, len(ings), 3):
                row = ings[i:i+3]
                print("  " + "".join(f"{item:<{col_width}}" for item in row))

        input(f"\n{Colors.DIM}Press Enter to return to main menu...{Colors.RESET}")

# -----------------------------------------------------------------------------
# Main Execution Entry Point
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        app = SmartRecipeApp()
        app.run()
    except (KeyboardInterrupt, EOFError):
        print(f"\n\n{Colors.GREEN}Application exited. See you next time! 🍳{Colors.RESET}")
        sys.exit(0)