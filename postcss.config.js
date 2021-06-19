const path = require('path');

module.exports = (ctx) => ({
    plugins: [
        require('tailwindcss')(path.resolve(__dirname, 'tailwind.config.js')),
        require('autoprefixer'),
        process.env.ENVIRONMENT === 'production' && require('@fullhuman/postcss-purgecss')({
            content: [
                /* To automatically scan all template directories (can be slower) */
                // path.resolve(__dirname, 'project/**/templates/**/*.html')

                /* or */

                /* To only scan specific directories (can be faster) */
                path.resolve(__dirname, 'project/pages/templates/pages/*.html'),
                path.resolve(__dirname, 'project/templates/*.html')
            ],
            defaultExtractor: content => content.match(/[A-Za-z0-9-_:/]+/g) || []
        })
    ],
});
