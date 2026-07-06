A Comprehensive Measure of Well-Being (HDI Prediction)

Overview

This project leverages Machine Learning to predict the Human Development Index (HDI) based on key socio-economic indicators such as income, education, and life expectancy. The goal is to move beyond GDP-based rankings and provide a more comprehensive, data-driven measure of a country's well-being using a trained regression model.

The project follows a structured SDLC-style workflow — from ideation through deployment and demonstration — with each phase documented in its own folder.

Live Application

🔗 https://hdiprediction-wwxrh4xzyjl8ybrs5gis9k.streamlit.app/

Key Features

Predictive Modeling – Trained regression model estimates HDI scores from socio-economic inputs. User-Friendly Interface – Simple, responsive web form for entering indicator values. Dynamic Results – Real-time prediction of HDI score and corresponding development category (Low / Medium / High / Very High). Cloud Deployment – Fully deployed and publicly accessible via Render.

Tech Stack

LayerTechnologyModeling & AnalysisPython, Jupyter Notebook, Scikit-Learn, Pandas, NumPyBackendPython (Flask)FrontendHTML5, CSS3, JavaScriptDeploymentRender

Repository Structure

This repository documents the project across its full development lifecycle:

├── 1.Brainstorming & Ideation/ # Problem statement, idea generation ├── 2.Requirement Analysis/ # Functional & non-functional requirements ├── 3.Project Design Phase/ # Data flow diagrams, architecture, UI design ├── 4.Project Planning Phase/ # Sprint/milestone planning ├── 5.Project Development Phase/ # Model training notebooks & app code ├── 6.Project Testing/ # Test cases and validation results ├── 7.Project Documentation/ # Final project report and supporting docs ├── 8.Project Demonstration/ # Demo video / screenshots └── README.md

Note: Model training and experimentation are primarily carried out in Jupyter Notebooks under the Development phase folder; the deployable web app (Flask backend + HTML/CSS frontend) is built from the resulting trained model.
