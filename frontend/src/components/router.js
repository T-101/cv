import React from 'react';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import LandingPageContainer from "./landingpagecontainer";
import WorkContainer from "./workcontainer";
import MeContainer from "./mecontainer";
import HobbyContainer from "./hobbycontainer";
import ContactContainer from "./contactcontainer";
import {getData} from './functions';


export default class CVRouter extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            realname: "",
            routes: {
                'welcome': {
                    'name': 'Welcome',
                    'url': '/'
                },
                'me': {
                    'name': 'Me',
                    'url': '/me'
                },
                'work': {
                    'name': 'Work',
                    'url': '/work'
                },
                'hobby': {
                    'name': 'Hobby',
                    'url': '/hobby'
                },
                'contact': {
                    'name': 'Contact',
                    'url': '/contact'
                }
            },
        };
    }

    async componentDidMount() {
        const url = window.location.protocol + '//' + window.location.hostname + ':8000/api/v1/info/info/me/';
        let json = await getData(url);
        this.setState({realname: json.real_name});
    }

    render() {

        return (
            <div className={this.props.width < this.props.responsiveBreakpoint ? "" : "container"}>
                {/* <BrowserRouter basename="/cv"> */}
                <BrowserRouter>
                    <Switch>
                        <Route exact path={this.state.routes.welcome.url}
                               render={(props) => (
                                   <LandingPageContainer {...this.state} {...this.props} {...props} />)}/>
                        <Route exact path={this.state.routes.me.url}
                               render={(props) => (
                                   <MeContainer {...this.state} {...this.props} {...props} />)}/>
                        <Route exact path={this.state.routes.work.url}
                               render={(props) => (
                                   <WorkContainer {...this.state} {...this.props} {...props} />)}/>
                        <Route exact path={this.state.routes.hobby.url}
                               render={(props) => (
                                   <HobbyContainer {...this.state} {...this.props} {...props} />)}/>
                        <Route exact path={this.state.routes.contact.url}
                               render={(props) => (
                                   <ContactContainer {...this.state} {...this.props} {...props} />)}/>
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}
