#  Cross-Browser & Cross-Device Testing Report

##  Project Overview
Tested the webpage:
https://shoplane-by-lassie.netlify.app/clothing.html

Testing was performed across multiple browsers and devices to identify:
- Layout issues
- Broken links
- Functionality discrepancies
- Compatibility problems

---

##  Browsers Tested

| Browser  | Version | Result |
|-----------|----------|---------|
| Chrome    | Latest   |  Working |
| Firefox   | Latest   |  Minor layout shift |
| Edge      | Latest   |  Working |
| Safari    | Latest   |  404 Error |

---

##  Devices Tested

| Device Type | Screen Size | Result |
|-------------|-------------|---------|
| Desktop     | 1920x1080   |  404 Page Not Found |
| Tablet      | 768x1024    |  Layout misalignment |
| Mobile      | 375x667     |  Navigation overlap |

---

##  Issues Identified

###  404 Page Not Found (Major Issue)
- The URL `/clothing.html` returns a **Netlify 404 error**
- Likely causes:
  - File not deployed
  - Incorrect file name (case-sensitive issue)
  - Wrong routing configuration

📸 Screenshot:  
![404 Error](./assets/404-error.png)

---

### 2️ Layout Issues on Tablet & Mobile
- Navigation menu overlaps content on small screens
- Images are not properly responsive
- Some sections overflow horizontally

---

###  Broken Links
- Internal links to product categories return 404
- Possible incorrect path references

---

##  Recommended Fixes

###  Fix 404 Error
- Ensure `clothing.html` exists in the root directory
- Check filename case (Netlify is case-sensitive)
- Redeploy site
- Add `_redirects` file if using SPA routing:

```
/*    /index.html   200
```

---

###  Improve Responsive Design
Add responsive meta tag in `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Use responsive CSS:

```css
img {
  max-width: 100%;
  height: auto;
}

@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
  }
}
```

---

###  Fix Broken Links
- Use relative paths correctly:
```html
<a href="clothing.html">Clothing</a>
```
- Avoid absolute paths unless necessary

---

##  Overall Compatibility Status

| Area            | Status |
|-----------------|--------|
| Desktop Layout  |  Needs Fix |
| Mobile Layout   |  Not Fully Responsive |
| Navigation      |  Overlap Issue |
| Page Routing    |  404 Error |
| Cross Browser   |  Minor Inconsistencies |

---

##  Conclusion

The webpage has:
- Major routing issue (404 error)
- Responsive design problems
- Minor cross-browser layout differences

After fixing routing and improving responsive CSS, compatibility across browsers and devices will significantly improve.

---

## Tested By
Arpan Banerjee  
Software Testing Practice Project  
2026
