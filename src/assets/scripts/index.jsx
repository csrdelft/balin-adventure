import React from "react";
import $ from "jquery";
import _ from "underscore";
import { render } from 'react-dom';
import { syncHistory, routeReducer } from 'react-router-redux';
import { combineReducers } from 'redux';
import * as immutable from 'immutable';

// useful for debuggin'
window._ = _;
window.$ = $;
window.immutable = immutable;

import configureStore from 'store/configureStore';
import history from 'store/history';

import App from 'containers/App';
import * as reducers from 'reducers';

let initialState = {};

let reducer = combineReducers(Object.assign({}, reducers, {routing: routeReducer}));
let store = configureStore(reducer, initialState);

render(<App store={store} history={history} /> , $('#mount-app')[0]);

