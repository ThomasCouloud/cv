import streamlit as st

def display_english_cv(selected_section):
    
    if selected_section == "Profile":
        st.header("Profile")
        st.write("""
As a French citizen, I am determined to pursue a doctorate abroad to broaden my professional horizons and increase my impact in my field. This decision is driven by the desire to integrate deep expertise with international experience.

My goal is to immerse myself in a diverse academic environment, to be exposed to new methodologies, and to collaborate with experts from various backgrounds. I am convinced that this will not only strengthen my technical skills but also enhance my ability to communicate and innovate in a multicultural context.

I am motivated by the opportunity to bring my unique perspective to the international community and to develop a global professional network. This journey is not just a quest for academic knowledge, but also a commitment to personal development, laying the groundwork for a rewarding and dynamic career on the global stage.

In summary, my ambition is to combine my training and experiences in France with an international educational experience, transforming myself into a well-rounded professional ready to make a significant contribution to my field at an international level.
    """)

    elif selected_section == "Skills":
        st.header("Skills")
        st.write("""
    - **Programming:** Python
             
    - **Data Visualization:** Matplotlib, Seaborn.
             
    - **Machine Learning:** Classification, Regression, Clustering with Scikit-Learn.
             
    - **Advanced Machine Learning:** Time Series Analysis, Text Mining, Dimensionality Reduction.
            
    - **Data Engineering:** Databases, SQL, PySpark.
             
    - **Deep Learning:** Neural Networks, ANN, CNN, and RNN with Keras, TensorFlow, PyTorch.    
             
    - **Advanced Programming:** Web Scraping, Bash Linux Programming, Git/GitHub, Unit Testing.
            
    - **DataOps-Isolation:** FastAPI, API Security, Docker, Flask, Bootstrap.
             
    - **DataOps-Orchestration:** Kubernetes, Airflow.
             
    - **ModelOps:** MLFlow and Data Culture.
             
    - **Business Intelligence:** PowerBI and Make.
             
    - **Data Culture and Governance:** Data Sources and Types, GDPR.
           
    - **Project Management:** Agile Methodology and related tools.
             
    """)

    elif selected_section == "Certification":
        st.header("Certification")
        st.write("""
    You can find skill certifications on my LinkedIn profile here: https://www.linkedin.com/in/thomas-couloud-b5628027a/             
    """)

    # Professional Experience Section
    elif selected_section == "Professional Experience":
        st.header("Professional Experience")
    
        st.subheader("Data Product Manager Curriculum Validation Project (RNCP Bloc 1 and 2)")
        st.write("""
    **Study of a fictional improvement of the LeBonCoin website (Datascientest):**
    Our goal was to propose an improvement of the LeBonCoin site integrating Machine Learning techniques. 
    We were tasked with leading and drafting several documents attesting to the interest of our product: business canvas, MVP, Experience Map, etc.
    """)
    
        st.subheader("Data Scientist Curriculum Validation Project (RNCP Bloc 3)")
        st.write("""
    **Heartbeat Classification (Datascientest):**
    Our goal was to predict whether a patient's electrocardiogram (ECG) is normal or abnormal. 
    We followed several phases, including data visualization, feature engineering, modeling with different machine learning models, and interpreting the decisions of the models to improve accuracy and interpretability. 
    [Link to the project on GitHub](https://github.com/ThomasCouloud/cv/tree/main/Heart%20beat%20project)
    """)
    
        st.subheader("MLOps Curriculum Validation Project (RNCP Bloc 4)")
        st.write("""
    **Deployment of a DowJones price prediction model (Datascientest):**
    Our goal was to develop an API incorporating a DowJones price prediction model. 
    We had to deploy this API using tools like FastAPI, Docker, and Kubernetes, automating model-related features: training, predictions, performance tracking, etc.
    """)

    # Internship Section
        st.subheader("Internship at Clid Systems and Snef Group")
        st.write("""
    **Design and implementation of robotic painting lines, from paint supply to drying, including varnish application.**
    Collaboration with clients such as Tesla, Ariane Espace, and Airbus Helicopters.
    """)

    # Preliminary Design
        st.subheader("Preliminary Design")
        st.write("""
    - **Development of specifications:** Define needs and requirements.
    - **Drafting of tenders:** If necessary, for the supply of products, services, and solutions.
    """)
    
    # Detailed Design
        st.subheader("Detailed Design")
        st.write("""
    - **Development of the execution dossier or digital model:** Of the whole or part of an automatic system.
    - **Selection of components:** Selecting the appropriate components.
    - **Validation with the client:** Ensuring that the chosen solutions meet expectations.
    """)

    # Implementation │ Fine-tuning
        st.subheader("Implementation │ Fine-tuning")
        st.write("""
    - **Installation of components:** Carry out the installation of components.
    - **Manufacturing and assembly:** Manufacture parts and assemble components.
    - **Wiring and testing:** Perform wiring, testing, adjustments, and fine-tuning.
    """)

    # Installation │ Commissioning
        st.subheader("Installation │ Commissioning")
        st.write("""
    - **Site organization:** Monitor the works and install the equipment.
    - **Commissioning:** Perform commissioning and operational testing.
    """)

    # Communication
        st.subheader("Communication")
        st.write("""
    - **Meetings:** Participate in meetings.
    - **Documentation:** Write documents and manage the document database.
    """)

    # Taking into Account Regulations and Technological Evolutions
        st.subheader("Taking into Account Regulations and Technological Evolutions")
        st.write("""
    - **Technological monitoring:** Participate in technological and documentary monitoring.
    - **Security policy and sustainable development:** Apply and contribute to the evolution of policies.
    """)

    elif selected_section == "Training":
        st.header("Training")
        st.subheader("RNCP Title 'Project Manager in Artificial Intelligence'")
        st.write("""
        - **Level:** 7 (equivalent to Master's)
        - **Institution:** Datascientest in partnership with Mines Paris and Sorbonne
        - **Specialty:** Engineering in Machine Learning
        - **Period:** March 2023 - November 2023
        - **[More information on the program]**(https://datascientest.com/formation-machine-learning-engineer)
        """)

        st.subheader("License (Bac+2)")
        st.write("""
        - **Institution:** University of Grenoble-Alpes
        - **Subjects:** Physics, Chemistry, Mathematics, and Mechanics
        - **Note:** Completed after three semesters (early cessation)
        - **Period:** 2019-2022
        - **[Link to the first year program]**(https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/licence-XA/licence-physique-IAI3PBC7//portail-physique-chimie-mecanique-mathematiques-1re-annee-valence-IK3VB0X4.html?search-keywords=pcmm)
        - **[Link to the second year program]**(https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/licence-XA/licence-physique-IAI3PBC7/parcours-physique-mecanique-mathematiques-2e-annee-valence-JVHTJKMX.html)
        """)

        st.subheader("BTS Design and Implementation of Automated Systems in Apprenticeship")
        st.write("""
        - **Institution:** UIMM CFAI LDA, Clid Systémes, Snef Group
        - **Period:** August 2022 - March 2023
        """)

    elif selected_section == "Languages":
        st.header("Languages")
        st.subheader("French")
        st.write("Level: Native")
        st.subheader("English")
        st.write("Level: B2 (2019)")
        st.subheader("Spanish")
        st.write("Level: B2 (2019)")

def display_french_cv(selected_section):
    
    if selected_section == "Profil":
        st.header("Profil")
        st.write("""
En tant que citoyen français, je suis résolu à poursuivre un doctorat à l'étranger pour élargir mes perspectives professionnelles et accroître mon impact dans mon domaine. Cette décision est guidée par le désir d'intégrer une expertise approfondie avec une expérience internationale.

Mon objectif est de me plonger dans un environnement académique diversifié, de m'exposer à de nouvelles méthodologies et de collaborer avec des experts de divers horizons. Je suis convaincu que cela renforcera non seulement mes compétences techniques, mais aussi ma capacité à communiquer et innover dans un contexte multiculturel.

Je suis motivé par l'opportunité d'apporter ma perspective unique à la communauté internationale et de développer un réseau professionnel global. Ce parcours n'est pas seulement une quête de connaissances académiques, mais aussi un engagement envers le développement personnel, préparant ainsi le terrain pour une carrière enrichissante et dynamique sur la scène mondiale.

En résumé, mon ambition est d'associer ma formation et mes expériences en France à une expérience éducative internationale, me transformant en un professionnel bien arrondi et prêt à contribuer de manière significative à mon domaine à l'échelle internationale.
             """)

    elif selected_section == "Compétences":
        st.header("Compétences")
        st.write("""
    - **Programmation:** Python
             
    - **Visualisation des données:** Matplotlib, Seaborn.
             
    - **Apprentissage automatique:** Classification, Régression, Clustering avec Scikit-Learn.
             
    - **Apprentissage automatique avancé:** Analyse de séries temporelles, Text Mining, Réduction de dimensions.
            
    - **Ingénierie des données:** Bases de données, SQL, PySpark.
             
    - **Apprentissage profond:** Réseaux neuronaux, ANN, CNN et RNN avec Keras, TensorFlow, PyTorch.    
             
    - **Programmation avancée:** Web Scraping, Programmation Bash Linux, Git/GitHub, Tests unitaires.
            
    - **DataOps-Isolation:** FastAPI, Sécurité API, Docker, Flask, Bootstrap.
             
    - **DataOps-Orchestration:** Kubernetes, Airflow.
             
    - **ModelOps:** MLFlow et Culture des données.
             
    - **Intelligence d'affaires:** PowerBI et Make.
             
    - **Culture et gouvernance des données:** Sources et types de données, RGPD.
           
    - **Gestion de projet:** Méthodologie Agile et outils correspondants.
             
    """)

    elif selected_section == "Certification":
        st.header("Certification")
        st.write("""
    Vous trouverez les certifications de compétence sur mon profil LinkeIn ici: https://www.linkedin.com/in/thomas-couloud-b5628027a/             
    """)

    # Section Expérience Professionnelle
    elif selected_section == "Expérience Professionnelle":
        st.header("Expérience Professionnelle")
    
        st.subheader("Projet de validation du cursus Data Product Manager (Bloc 1 et 2 RNCP)")
        st.write("""
    **Etude d'une amélioration (fictive) du site LeBonCoin (Datascientest):**
    Notre objectif était de proposer une amélioration du site LeBonCoin intégrant des techniques de Machine Learning. 
    Nous devions mener et rédiger plusieurs documents attestants de l'intérêt de notre produit: business canvas, MVP, Experience Map, etc.
    """)
    
        st.subheader("Projet de validation du cursus Datascientist (Bloc 3 RNCP)")
        st.write("""
    **Classification des battements cardiaques (Datascientest):**
    Notre objectif était de prédire si un électrocardiogramme (ECG) d'un patient est normal ou anormal. 
    Nous avons suivi plusieurs phases, dont la visualisation des données, l'ingénierie des caractéristiques, la modélisation avec différents modèles de machine learning, et l'interprétation des décisions des modèles pour améliorer la précision et l'interprétabilité. 
    [Lien vers le projet sur GitHub](https://github.com/ThomasCouloud/cv/tree/main/Heart%20beat%20project)
    """)
    
        st.subheader("Projet de validation du cursus MLOps (Bloc 4 RNCP)")
        st.write("""
    **Déploiement d'un modèle de prédiction des cours du DowJones (Datascientest):**
    Notre objectif était de développer une API intégrant un modèle de prédiction des cours du DowJones. 
    Nous devions déployer cette API avec des outils comme FastAPI, Docker ou encore Kubernetes en automatisant les fonctionnalités liées au modèle: entraînement, prédictions, suivi des performances, etc.
    """)

    # Section Alternance
        st.subheader("Alternance chez Clid Systèmes et Snef Group")
        st.write("""
    **Conception et mise en œuvre de lignes de peinture robotisées, depuis l'approvisionnement en peinture jusqu'au séchage, y compris l'application de vernis.**
    Collaboration avec des clients tels que Tesla, Ariane Espace, et Airbus Helicopters.
    """)

    # Conception Préliminaire
        st.subheader("Conception Préliminaire")
        st.write("""
    - **Élaboration du cahier des charges:** Définir les besoins et les exigences.
    - **Rédaction des appels d’offres:** Si nécessaire, pour la fourniture de produits, services et solutions.
    """)

    # Conception Détaillée
        st.subheader("Conception Détaillée")
        st.write("""
    - **Élaboration du dossier de réalisation ou modèle numérique:** De tout ou partie d’un système automatique.
    - **Choix des constituants:** Sélectionner les composants adéquats.
    - **Validation avec le client:** S'assurer que les solutions retenues répondent aux attentes.
    """)

    # Réalisation │ Mise au point
        st.subheader("Réalisation │ Mise au point")
        st.write("""
    - **Implantation des constituants:** Réaliser l'implantation des constituants.
    - **Fabrication et assemblage:** Fabriquer les pièces et assembler les composants.
    - **Câblage et tests:** Réaliser les câblages, les tests, les réglages et les mises au point.
    """)

    # Installation │ Mise en service
        st.subheader("Installation │ Mise en service")
        st.write("""
    - **Organisation du chantier:** Suivre les travaux et installer les équipements.
    - **Mise en service:** Réaliser la mise en service et effectuer les essais en fonctionnement.
    """)

    # Communication
        st.subheader("Communication")
        st.write("""
    - **Réunions:** Participer aux réunions.
    - **Documentation:** Rédiger les documents et gérer la base documentaire.
    """)

    # Prise en Compte de la Réglementation et Évolutions Technologiques
        st.subheader("Prise en Compte de la Réglementation et Évolutions Technologiques")
        st.write("""
    - **Veille technologique:** Participer à la veille technologique et documentaire.
    - **Politique de sécurité et développement durable:** Appliquer et participer à l'évolution des politiques.
    """)

    elif selected_section == "Formation":
        st.header("Formation")
        st.subheader("Titre RNCP 'chef de projet en intelligence artificielle'")
        st.write("""
        - **Niveau:** 7 (équivalent Master)
        - **Institution:** Datascientest en partenariat avec Mines Paris et Sorbonne
        - **Spécialité:** Ingénierie en Machine Learning
        - **Période:** Mars 2023 - Novembre 2023
        - **[Plus d'informations sur le programme]**(https://datascientest.com/formation-machine-learning-engineer)
        """)


        st.subheader("Licence (Bac+2)")
        st.write("""
        - **Institution:** Université Grenoble-Alpes
        - **Matières:** Physique, Chimie, Mathématiques, et Mécanique
        - **Remarque:** Terminé après trois semestres (arrêt précoce)
        - **Période:** 2019-2022
        - **[Lien vers le programme de première année]**(https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/licence-XA/licence-physique-IAI3PBC7//portail-physique-chimie-mecanique-mathematiques-1re-annee-valence-IK3VB0X4.html?search-keywords=pcmm)
        - **[Lien vers le porgramme de deuxième année]**(https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/licence-XA/licence-physique-IAI3PBC7/parcours-physique-mecanique-mathematiques-2e-annee-valence-JVHTJKMX.html)
        """)


        st.subheader("BTS Conception et réalisation de systèmes automatisés en alternance")
        st.write("""
        - **Institution:** UIMM CFAI LDA, Clid Systémes, Snef Group
        - **Période:** Août 2022 - Mars 2023
        """)

    elif selected_section == "Langues":
        st.header("Langues")
        st.subheader("Français")
        st.write("Niveau: natif")
        st.subheader("Anglais")
        st.write("Niveau: B2 (2019)")
        st.subheader("Espagnol")
        st.write("Niveau: B2 (2019)")

def main():
   
    st.markdown("<h1 style='text-align: center; color: white; font-size: 60px;'>Thomas Couloud</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 80px;'>Curriculum Vitae</h1>", unsafe_allow_html=True)

    st.sidebar.title("Language Selection")
    choice = st.sidebar.radio("Choose a language", ["English", "French"])

    if choice == "English":
        sections = ["Profile", "Skills", "Certifications", "Professional Experience", "Training", "Languages"]
        selected_section = st.selectbox("Choose the section to display", sections)
        display_english_cv(selected_section)
    else:
        sections = ["Profil", "Compétences", "Certification", "Expérience Professionnelle", "Formation", "Langues"]
        selected_section = st.selectbox("Choisissez la partie à afficher", sections)
        display_french_cv(selected_section)


if __name__ == "__main__":
    main()