module.exports = {
  content: ['build/base.html'], // see scripts/compile_css.bash
  media: false, // or 'media' or 'class'
  theme: {
    extend: {
      maxWidth: {
        'logo': '10rem'
       },
      maxHeight: {
        'logo': '5rem'
       }
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
