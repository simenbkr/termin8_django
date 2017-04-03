// http://webpack.github.io
'use strict';

var path = require('path');
var webpack = require('webpack');

module.exports = {
   entry:  [
       'babel-polyfill',
       './static/src/app.js',
       './static/src/style.less',
   ],
   output:  {
       path: './static/dev',
       filename: 'build.js'
   },
   resolve: {
        extensions: ['', '.js', '.jsx', '.scss'],
        modulesDirectories: [
            'node_modules'
        ]
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                loader: ['babel'],
                include: [
                    path.resolve(__dirname, "static")
                ],
                query: {
                    plugins: ['transform-runtime'],
                    presets: ['es2015', 'stage-0', 'react']
                }
            },
            {
                test: /\.less$/,
                loader: "style!css!less"
            }
        ]
    }
};
