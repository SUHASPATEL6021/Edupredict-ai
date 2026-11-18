# Deployment guide

This project is a Streamlit application and can be deployed from its public GitHub repository.

1. Open https://share.streamlit.io/ and sign in with GitHub.
2. Select **Create app** → **Deploy a public app from GitHub**.
3. Choose this repository and branch `main`.
4. Set the main file path to `app.py`.
5. Deploy. The platform installs dependencies from `requirements.txt`.
6. Open the deployed app, exercise its main controls, and copy the working URL.
7. In GitHub, add the deployed URL under repository **About → Website**.
8. Capture a screenshot from the running app and add it to the README.

## Before sharing
- Confirm the GitHub Actions validation workflow passes.
- Confirm the app runs without an exception on first load.
- Confirm charts, controls, and downloads work.
- Do not claim simulated data is live sensor data or real student data.
- Do not upload private resumes or other personal information to public repositories.

**AtmosIQ:** Serial-connected hardware logging runs locally on your computer; the cloud dashboard can visualize uploaded logs but cannot directly access your local Arduino serial port.

**CareerForge:** The analyzer uses keyword matching, not an external generative AI model or a validated ATS scoring engine.
