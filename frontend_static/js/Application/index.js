import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter, Switch, Route, Link} from 'react-router-dom';

const Home = () => (
    <div>
        <h1>Welcome to the Tornadoes Website!</h1>
    </div>
);
const Schedule = () => (
    <div>
        <h1>Schedule</h1>
        <ul>
            <li>Timeline 1</li>
            <li>Timeline 2</li>
            <li>Timeline 3</li>
            <li>Timeline 4</li>
        </ul>
    </div>
);


const Main = () => (
    <main>
        <Switch>
            <Route exact path='/' component={Home}/>
            <Route path='/schedule' component={Schedule}/>
        </Switch>
    </main>
);

const App = () => (
    <div>
        <Main/>
    </div>
);


ReactDOM.render(
    <BrowserRouter>
        <App/>
    </BrowserRouter>,
    document.getElementById('app')
);