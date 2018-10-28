import React, {Component} from 'react';
import './App.css';
import CVRouter from "./components/router";

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            responsiveBreakpoint: 800,
        }
    }

    componentDidMount() {
        this.updateWindowDimensions();
        window.addEventListener('resize', this.updateWindowDimensions.bind(this));
    }

    componentWillUnmount() {
        window.removeEventListener('resize', this.updateWindowDimensions.bind(this));
    }

    updateWindowDimensions() {
        this.setState({width: window.innerWidth, height: window.innerHeight});
    }

    render() {
        return (
            <CVRouter {...this.state}/>
        );
    }
}

export default App;
