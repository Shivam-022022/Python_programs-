import re

references = """
[1] Smith, J. and Rao, P. (2019). Deep learning for crop yield. Nature Methods.
    doi:10.1038/s41592-019-0001-4. Contact: j.smith@university.edu
[2] Gupta, A. (2021). Graph networks in chemistry. J. Chem. Inf. Model.
    https://doi.org/10.1021/acs.jcim.1c00123  Email: agupta@research.org.in
[3] Lee, K. et al. (2023). Attention is useful. Available at https://arxiv.org/abs/2301.12345
    DOI: 10.1145/3580305.3599555, lee.k@cs.example.com
"""

dois = [d.rstrip(".,;") for d in re.findall(r"\b10\.\d{4,9}/[^\s,;]+", references)]
years = re.findall(r"\((\d{4})\)", references)
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}", references)
urls = [u.rstrip(".,;)") for u in re.findall(r"https?://[^\s<>]+", references)]

print("DOIs  :", dois)
print("Years :", years)
print("Emails:", emails)
print("URLs  :", urls)
