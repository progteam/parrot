// Based on
//  https://gist.github.com/int128/e0cdec598c5b3db728ff35758abdbafd 
process.env.NODE_ENV = 'development';

const fs = require('fs-extra');
const paths = require('react-scripts/config/paths');
const webpack = require('webpack');
const configFactory = require('react-scripts/config/webpack.config');
const config = configFactory('development');

// removes react-dev-utils/webpackHotDevClient.js at first in the array
config.entry.shift();

webpack(config).watch({}, (err, stats) => {
  if (err) {
    console.error(err);
  }
  console.error(stats.toString({
    chunks: true,
    colors: true
  }));
});
