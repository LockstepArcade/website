# Lockstep Arcade Website

This is a static website for Lockstep Arcade, built with clean HTML, CSS, and integration with Web3Forms for the beta access request form.

## Files Included

- `index.html` - Main landing page with game info, features, screenshots, and beta signup form
- `setup.html` - Complete installation and setup guide
- `changelog.html` - Version history and changelog
- `styles.css` - All styling for the website
- `banner.jpg` - Banner image
- `screenshot1.png`, `screenshot2.png`, `screenshot3.png` - Game screenshots
- `lemmings_client_release_0.0.7.zip` - Downloadable game client

## Setup Instructions

### 1. Web3Forms Configuration

The contact form on the homepage uses Web3Forms. To make it work:

1. Go to https://web3forms.com/
2. Sign up for a free account
3. Create a new form and get your access key
4. Open `index.html` and find this line (around line 160):
   ```html
   <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
   ```
5. Replace `YOUR_ACCESS_KEY_HERE` with your actual Web3Forms access key

### 2. Deployment Options

This is a static website and can be hosted on various platforms:

#### GitHub Pages (Free)
1. Create a GitHub repository
2. Upload all files to the repository
3. Go to Settings > Pages
4. Select the branch to deploy from
5. Your site will be live at `https://yourusername.github.io/repository-name`

#### Netlify (Free)
1. Sign up at https://www.netlify.com/
2. Drag and drop the website folder
3. Your site will be live instantly with a custom URL
4. You can add a custom domain if desired

#### Vercel (Free)
1. Sign up at https://vercel.com/
2. Import your project (from GitHub or upload directly)
3. Deploy with one click

#### Any Static Hosting
You can also use:
- Cloudflare Pages
- GitLab Pages
- AWS S3 + CloudFront
- Traditional web hosting (just upload via FTP)

### 3. Testing Locally

To test the website locally:

1. Simply open `index.html` in your web browser
2. Or use a local server (recommended for full testing):
   ```bash
   # Using Python
   python -m http.server 8000

   # Using Node.js
   npx serve
   ```
3. Navigate to `http://localhost:8000` in your browser

## Customization

### Updating Content

- **Game version**: Update version numbers in `index.html` (download section) and `changelog.html`
- **Screenshots**: Replace `screenshot1.png`, `screenshot2.png`, `screenshot3.png` with new images
- **Banner**: Replace `banner.jpg` with a new banner image
- **Release file**: Replace `lemmings_client_release_0.0.7.zip` with the new release and update the filename in `index.html`

### Styling

All styles are in `styles.css`. The design uses CSS variables for easy theming:

```css
:root {
    --primary-color: #2563eb;
    --primary-dark: #1e40af;
    --secondary-color: #64748b;
    --accent-color: #f59e0b;
    /* ... more variables */
}
```

Change these values to customize the color scheme.

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with smooth animations
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Fast Loading**: Optimized assets and minimal dependencies
- **Contact Form**: Integrated with Web3Forms for beta access requests
- **Easy Navigation**: Clear structure with smooth scrolling

## Form Submissions

When users submit the beta access form, you'll receive an email notification with:
- Name
- Email address
- Preferred player name (if provided)
- Additional information (if provided)
- Whether they want email notifications

You can then send them the `credentials.bin` file manually via email.

## Future Enhancements

Consider adding:
- Gallery lightbox for screenshots
- FAQ section
- Community/Discord integration
- Video trailers or gameplay footage
- Blog/news section for updates

## Browser Support

The website works on all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## License

Customize as needed for your project.
