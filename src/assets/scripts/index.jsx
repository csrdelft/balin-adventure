import React from "react";
import $ from "jquery";
import { render } from 'react-dom';
import { syncReduxAndRouter, routeReducer } from 'redux-simple-router';
import { combineReducers } from 'redux';

import configureStore from 'store/configureStore';
import history from 'store/history';

import App from 'containers/App';
import * as reducers from 'reducers';

let initialState = {};

let reducer = combineReducers(Object.assign({}, reducers, {routing: routeReducer}));
let store = configureStore(reducer, initialState);

// make sure the router state is saved in the store
syncReduxAndRouter(history, store);

render(<App store={store} history={history} /> , $('#mount-app')[0]);

