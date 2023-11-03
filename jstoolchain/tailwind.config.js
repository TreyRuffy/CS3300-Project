/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../cs3300_project/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
