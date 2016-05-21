import React, { PropTypes } from 'react';
import { Router, Route, IndexRoute, Link } from 'react-router';
import { MainLayout, LogicListLayout, LogicLayout } from '../components/App';
import NotFound from '../components/NotFound';

const Routes = ({ history }) =>
  <Router history={history}>
	<Route path="/" component={MainLayout}>
		<IndexRoute component={LogicListLayout} />
		<Route path="logic/:id" component={LogicLayout} />
	</Route>
	<Route path="*" component={NotFound}/>
  </Router>;

Routes.propTypes = {
  history: PropTypes.any,
};

export default Routes;
