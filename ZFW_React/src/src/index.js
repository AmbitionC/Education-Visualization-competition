import React from 'react';
import ReactDOM from 'react-dom';
// import { HashRouter as Router, Route } from 'react-router-dom';
// import Home from './containers/Home';
import Main from './containers/Main';
// import * as serviceWorker from './serviceWorker';

// class App extends React.Component {
//     render() {
//         return (
//             <Router>
//                 <Route exact path='/' component={Home}/>
//                 <Route path='/main' component={Main}/>
//             </Router>
//         );
//     }
// }

ReactDOM.render(<Main />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
// serviceWorker.unregister();
