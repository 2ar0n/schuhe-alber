module.exports = {
  purge: {
      enabled: true,
      content: [
        'build/base.html', // see scripts/compile_css.bash
      ],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
