var path = require('path');
var webpack = require('webpack');

module.exports = {
    entry: './javascript/index.js',
    output: {
        path: __dirname + '/static/js',
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            {
                test: /.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            }
        ]
    }
};