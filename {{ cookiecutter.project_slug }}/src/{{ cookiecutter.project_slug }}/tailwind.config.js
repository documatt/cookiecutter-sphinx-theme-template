/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./styles/**/*.css",
    "./scripts/**/*.js",
    // Jinja templates
    "./theme/**/*.html",
    // exclude node_modules/
    "!./node_modules/**",
  ],
  theme: {},
  plugins: [require("@tailwindcss/typography")],
};
