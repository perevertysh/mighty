let mix = require('laravel-mix');

mix.webpackConfig({
    devtool: "inline-source-map",
    resolve: {
      modules: [
        path.resolve('./node_modules')
      ],
      alias: {
        core: path.resolve('./js/'),
        page: path.resolve('./page/'),
        assets: path.resolve('./static/'),
      }
    }
}).setResourceRoot('../')
  .js('./js/app.js', '../static/js/')
  .sass('./scss/app.scss', '../static/css/')
  .setPublicPath('../static/')
  .copyDirectory('static', '../static');
  
  module.exports = {
    rules: [
      {
        test: /\.s(c|a)ss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            // Requires sass-loader@^7.0.0
            options: {
              implementation: require('sass'),
              fiber: require('fibers'),
              indentedSyntax: true // optional
            },
            // Requires sass-loader@^8.0.0
            options: {
              implementation: require('sass'),
              sassOptions: {
                fiber: require('fibers'),
                indentedSyntax: true // optional
              },
            },
          },
        ],
      },
    ],
  }