import React from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import LandingPageContainer from "./LandingPageContainer";
import MeContainer from './MeContainer';
import WorkContainer from './WorkContainer'
import HobbyContainer from './HobbyContainer'
import ContactContainer from './ContactContainer'

export default function RouterComponent(props) {
    return (
        <Router>
            {props.children}
            <Switch>
                <Route exact path="/">
                    <LandingPageContainer/>
                </Route>
                <Route exact path="/me">
                    <MeContainer/>
                </Route>
                <Route exact path="/work">
                    <WorkContainer/>
                </Route>
                <Route exact path="/hobby">
                    <HobbyContainer/>
                </Route>
                <Route exact path="/contact">
                    <ContactContainer/>
                </Route>
            </Switch>
        </Router>
)
}
