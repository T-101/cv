import React from "react";
import Navbar from "./navbar";
import {getData} from './functions';


export default class PartyTableContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            image: ''
        };
    }

    async componentWillMount() {
        let url = window.location.protocol + '//' + window.location.hostname + ':8000/api/v1/info/info/me/';
        this.setState({data: await getData(url)});
        url = window.location.protocol + '//' + window.location.hostname + ':8000/api/v1/info/pictures/random/';
        const random = await getData(url);
        this.setState({image: random.image});
    }

    render() {
        let title = this.state.data.title;
        let email = 'No email specified';
        let phone = 'No phone number specified';
        try {
            email = this.state.data.emails ? this.state.data.emails[0].address : null;
        } catch (e) {
            console.log(e)
        }
        try {
            phone = this.state.data.phone_numbers ? this.state.data.phone_numbers[0].number : null;
        } catch (e) {
            console.log(e)
        }
        return (
            <div>
                <div className="bs-component">
                    <Navbar {...this.props} />
                </div>
                <div className={this.props.width < this.props.responsiveBreakpoint ? "container" : ""}>
                    <div className="row">

                        <div className="col-sm">
                            <div className="card border-secondary mb-3">
                                <div className="card-body">
                                    <h4 className="card-title">{title}</h4>

                                    <p className="card-text">
                                        <a href={"mailto:" + email}>{email}</a>
                                    </p>
                                    <p className="card-text">
                                        {phone}
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="col-sm">
                            <div className="card border-secondary mb-3">
                                <div className="card-body">
                                    <img className="img-fluid" src={this.state.image} alt="Antti Rummukainen" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

}
