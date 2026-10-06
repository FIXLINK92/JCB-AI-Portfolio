# Publish to GitHub

Recommended first step: publish this repository as **private**, review every screenshot/file, then deliberately switch it to public only when you are satisfied that no confidential material is included.

## Windows PowerShell

After extracting the folder to `C:\Users\ASUS\JCB-AI-Portfolio`:

```powershell
cd C:\Users\ASUS\JCB-AI-Portfolio

git init
git branch -M main
git add .
git commit -m "Create JCB AI portfolio"

gh repo create FIXLINK92/JCB-AI-Portfolio --private --source . --remote origin --push
```

## Review Before Making Public

Confirm that the repository contains no:

- `.env` files or credentials
- tokens or API keys
- real customer or employer information
- confidential TAG vehicle data
- private infrastructure details
- proprietary production source code

When the portfolio is ready for recruiter viewing:

```powershell
gh repo edit FIXLINK92/JCB-AI-Portfolio --visibility public
```

GitHub may require an additional visibility-change confirmation depending on CLI/version/account settings.

## Alternative: Keep Private

If the portfolio must remain private, do not assume a personal-account collaborator is strictly read-only. For controlled organization-level read access, move/create the portfolio under a GitHub Organization and assign the reviewer the **Read** repository role.
