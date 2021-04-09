module.exports = {
  mode: "jit",
  purge: {
      enabled: true,
      content: [
        'build/base.html', // see scripts/compile_css.bash
      ],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
    maxWidth: {
      '1/2': '50%',
     }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
