---
title: Beyond Input Attribution
---

## A Hands-On Tutorial to Concept-Based Explainable AI and Mechanistic Interpretability  
KDD 2025 | Toronto, Canada | August 3–7, 2025  

**Eliana Pastor**, Politecnico di Torino  
**Eleonora Poeta**, Politecnico di Torino  
**André Panisson**, CENTAI Institute  
**Alan Perotti**, CENTAI Institute  
**Gabriele Ciravegna**, CENTAI Institute


As deep learning systems become embedded in high-stakes domains, the demand for **transparent, trustworthy, and human-aligned AI** is more critical than ever. While traditional feature attribution methods like SHAP and LIME have long dominated the Explainable AI (XAI) landscape, they often fall short in robustness, fidelity, and alignment with how humans reason about decisions.
This hands-on tutorial introduces two powerful and complementary approaches that go beyond traditional feature attribution: **Concept-Based Explainable AI (C-XAI)** and **Mechanistic Interpretability**.

**C-XAI** offers explanations grounded in **high-level, domain-relevant concepts**, enabling users to interpret, manipulate, and reason about model behavior in ways that mirror human cognition. **Mechanistic interpretability**, on the other hand, is an emerging field that seeks to **reverse-engineer the internal structure of neural networks**, uncovering the circuits and representations that drive model decisions—often without relying on predefined concepts or labeled data.


Through a mix of **interactive coding sessions and guided exercises**, participants will explore and implement both paradigms. By the end of the session, attendees will walk away with a **modern interpretability toolbox** and the practical skills to apply it, making AI systems more transparent, reliable, and aligned with human values.


### Goals

- Discover how networks can learn human-interpretable concepts
- Discover how mechanistic interpretability can unveil internal model structures.
- Get hands-on with techniques like CBM, TCAV, Label Free CBM, Discover-Then-Name, and SAEuron.


---

# Prerequisites

Participants should have:

- Basic knowledge of machine learning and deep learning
- Familiarity with Python and PyTorch
- Comfortable with running Jupyter/Colab notebooks

No installation is required. All code will run on Google Colab.

---

# Tutorial Schedule & Structure

### ⏱️ Duration: 3 hours (with breaks)

| Section | Topic | Duration |
|--------|--------|----------|
| 1️⃣ | Introduction to Explainable AI | 15 min |
| 2️⃣ | Concept-Based XAI (C-XAI) | 75 min |
| 3️⃣ | Mechanistic Interpretability | 75 min |
| 4️⃣ | Wrap-up & Discussion | 15 min |

---

## 🧠 1. Introduction to Explainable AI

Overview of XAI and limitations of feature attribution techniques like SHAP or LIME. Motivation for human-aligned explanations.

---

## 🪞 2. Concept-Based XAI (C-XAI)

### 🧩 By-Design Models
- Concept Bottleneck Models (CBMs)
- Label-Free CBMs with CLIP

### 🔍 Post-hoc Methods
- TCAV (Testing with Concept Activation Vectors)
---

## 🔬 3. Mechanistic Interpretability

- Sparse Autoencoders (SAEs)
- Discover-Then-Name
- SAEuron for intervention and behavior steering
- Concepts: Superposition, Monosemanticity

---

## 💬 4. Wrap-up

- Takeaways
- Open Q&A
- Future research opportunities

---

# Hands-On: Colab Notebooks

All notebooks will run on **Google Colab** – no local setup required.  
Click below to launch:

- [🔗 C-XAI: Testing with Concept Activation Vectors (TCAV)](https://github.com/cxai-mechint-htutorial-kdd2025/cxai-mechint-htutorial-kdd2025.github.io/blob/main/notebooks/01_tcav.ipynb)
- [🔗 C-XAI: Concept Bottleneck Model (CBM)](https://github.com/cxai-mechint-htutorial-kdd2025/cxai-mechint-htutorial-kdd2025.github.io/blob/main/notebooks/02a_cbm.ipynb)
- [🔗 C-XAI: Label Free Concept Bottleneck Model (LF-CBM)](https://github.com/cxai-mechint-htutorial-kdd2025/cxai-mechint-htutorial-kdd2025.github.io/blob/main/notebooks/02b_label_free_cbm.ipynb)
- [🔗 Mechanistic: Discover-Then-Name](https://github.com/cxai-mechint-htutorial-kdd2025/cxai-mechint-htutorial-kdd2025.github.io/blob/main/notebooks/03_discover_then_name.ipynb)
- [🔗 Mechanistic: SAEuron](https://colab.research.google.com/...)

Each notebook includes:
- Step-by-step explanations
- Starter code
- Evaluation and visualization cells

---
# Organizers

<div style="display: flex; align-items: center; margin-bottom: 1em;">

  <a href="https://elianap.github.io/">
    <img src="https://smartdata.polito.it/wp-content/uploads/2018/01/pastor_photo-274x300.png" alt="Eliana Pastor" width="80" style="border-radius: 50%; margin-right: 15px;" />
  </a>

  <div>
    <strong>Eliana Pastor</strong><br>
    Assistant Professor, Politecnico di Torino<br>
    <em>Research:</em> Trustworthy AI, Explainability, Fairness 
  </div>

</div>

<div style="display: flex; align-items: center; margin-bottom: 1em;">

  <a href="https://www.polito.it/personale?p=052068">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQS_5JjylSEbXBdNg9L45j0R6_1KUoqKcgBZQ&s" alt="Eleonora Poeta" width="80" style="border-radius: 50%; margin-right: 15px;" />
  </a>

  <div>
    <strong>Eleonora Poeta</strong><br>
    PhD Student, Politecnico di Torino<br>
    <em>Research:</em> Concept-based explainability, robustness
  </div>

</div>

<div style="display: flex; align-items: center; margin-bottom: 1em;">

  <a href="https://andre.panisson.com/">
    <img src="https://centai.eu/assets/images/people/panisson.webp" alt="André Panisson" width="80" style="border-radius: 50%; margin-right: 15px;" />
  </a>

  <div>
    <strong>André Panisson</strong><br>
    Principal Researcher, CENTAI  <br>
    <em>Lead of Responsible AI Team</em> 
  </div>

</div>

<div style="display: flex; align-items: center; margin-bottom: 1em;">
    <img src="https://centai.eu/assets/images/people/perotti.webp" alt="Alan Perotti" width="80" style="border-radius: 50%; margin-right: 15px;" />

  <div>
    <strong>Alan Perotti</strong><br>
    Senior Researcher, CENTAI  <br>
    <em>Focus:</em> XAI applications in finance (Intesa Sanpaolo)
  </div>

</div>

<div style="display: flex; align-items: center; margin-bottom: 1em;">
    <img src="https://dbdmg.polito.it/dbdmg_web/wp-content/uploads/2023/10/GabrieleCiravegna-3.jpg" alt="Gabriele Ciravegna" width="80" style="border-radius: 50%; margin-right: 15px;" />

  <div>
    <strong>Gabriele Ciravegna</strong><br>
    Researcher, CENTAI  <br>
    <em>Focus:</em> Mechanistic interpretability, reliability
  </div>

</div>




## 📚 References

[1] Ciravegna, G., Espinosa Zarlenga, M., Barbiero, P., Giannini, F., Shams, Z., Garreau, D., Jamnik, M., & Cerquitelli, T. (2024). Workshop on Human-Interpretable AI. In *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, 6708–6709.

[2] Cywiński, B., & Deja, K. (2025). SAeUron: Interpretable Concept Unlearning in Diffusion Models with Sparse Autoencoders. *arXiv:2501.18052*.

[3] Espinosa Zarlenga, M., Barbiero, P., Ciravegna, G., Marra, G., Giannini, F., Diligenti, M., Shams, Z., Precioso, F., Melacci, S., Weller, A., et al. (2022). Concept embedding models: Beyond the accuracy-explainability trade-off. In *Advances in Neural Information Processing Systems*, 35, 21400–21413.

[4] Gade, K., Geyik, S. C., Kenthapadi, K., Mithal, V., & Taly, A. (2020). Explainable AI in industry: Practical challenges and lessons learned: Implications tutorial. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency*, 699–699.

[5] Kim, B., Wattenberg, M., Gilmer, J., Cai, C., Wexler, J., Viegas, F., et al. (2018). Interpretability beyond feature attribution: Quantitative testing with concept activation vectors (TCAV). In *International Conference on Machine Learning*, PMLR, 2668–2677.

[6] Koh, P. W., Nguyen, T., Tang, Y. S., Mussmann, S., Pierson, E., Kim, B., & Liang, P. (2020). Concept bottleneck models. In *International Conference on Machine Learning*, PMLR, 5338–5348.

[7] Maurer, M. C., Metsch, J. M., Hempel, P., Bender, T., Spicher, N., & Hauschild, A.-C. (2024). Explainable Artificial Intelligence on Biosignals for Clinical Decision Support. In *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*.

[8] Mayer, M. C., Zafar, M. B., Franceschi, L., & Rangwala, H. (2023). Hands-on Tutorial: "Explanations in AI: Methods, Stakeholders and Pitfalls". In *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*.

[9] Oikarinen, T., Das, S., Nguyen, L. M., & Weng, T.-W. (2023). Label-free concept bottleneck models. *arXiv preprint arXiv:2304.06129*.

[10] Poeta, E., Ciravegna, G., Pastor, E., Cerquitelli, T., & Baralis, E. (2023). Concept-based explainable artificial intelligence: A survey. *arXiv preprint arXiv:2312.12936*.

[11] Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., et al. (2021). Learning transferable visual models from natural language supervision. In *International Conference on Machine Learning*, PMLR, 8748–8763.

[12] Rao, S., Mahajan, S., Böhle, M., & Schiele, B. (2024). Discover-then-name: Task-agnostic concept bottlenecks via automated concept discovery. In *European Conference on Computer Vision*, Springer, 444–461.
