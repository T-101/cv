import React from "react";
import Navbar from "./navbar";
import DetailDataRow from "./detaildatarowcontainer";
import {getData} from './functions';


export default class MeContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            stateRoute: '',
            stateRouteName: '',
            data: []
        };

    }

    async componentDidMount() {

        const url = window.location.protocol + '//' + window.location.hostname + ':8000/api/v1/info/details/';
        this.setState({data: await getData(url)});

        const routes = this.props.routes;
        for (let route in routes) {
            if (routes.hasOwnProperty(route)) {
                if (this.props.match.path === routes[route].url) {
                    this.setState({
                        'stateRoute': route,
                        'stateRouteName': routes[route].name
                    })
                }
            }
        }
    }

    render() {
        return (
            <div>
                <div className="bs-component">
                    <Navbar {...this.props} />
                </div>
                <div className={this.props.width < this.props.responsiveBreakpoint ? "container" : ""}>
                    <div className="row">
                        <div className="col-12">


                            <div className="card mb-3">
                                <h3 className="card-header">{this.state.stateRouteName}</h3>

                                {this.state.data ? this.state.data.map((dataitem, d) => {
                                    return (
                                        <DetailDataRow key={d} dataitem={dataitem}/>
                                    )
                                }) : null}

                            </div>

                        </div>
                    </div>
                </div>
            </div>
        )
    }

}
