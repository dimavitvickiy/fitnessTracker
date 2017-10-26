import React from 'react';
import { Switch, Route } from 'react-router-dom';

import { Home } from '../Home';
import { Schedule } from '../Schedule';


export const Main = () => (
    <div>
        <Switch>
            <Route exact path='/' component={Home}/>
            <Route path='/schedule' component={Schedule}/>
        </Switch>
    </div>
);
