import React from 'react';
import ReactDOM from 'react-dom';


class Application extends React.Component {
    render() {
        return (
            <div>
                <h1>Fitness Tracker Application from React 16</h1>
                <button className="btn btn-outline-primary">Start my tracker!</button>
            </div>
        )
    }
}


ReactDOM.render(
    <Application/>,
    document.getElementById('app')
);