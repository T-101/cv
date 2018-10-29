import React from "react";
import Navbar from "./navbar";
import {getData, getUrl} from './functions';


class TableRow extends React.Component {
    render() {

        let href = this.props.value.url;
        let faClass = 'fa fa-2x fa-fw fa-' + this.props.value.url_type;
        let title = this.props.value.title;
        let type = '';

        switch (this.props.type) {
            case 'email': {
                href = 'mailto:' + this.props.value.address;
                faClass = 'fa fa-2x fa-fw fa-envelope-square';
                title = this.props.value.address;
                break;
            }
            case 'phone': {
                href = 'tel:' + this.props.value.number.replace(/-()/g, '');
                faClass = 'fa fa-2x fa-fw fa-phone-square';
                title = this.props.value.number;
                type = '(' + this.props.value.type + ')';
                break;
            }
            default:
        }

        return (
            <tr>
                <td>
                    <a href={href}><i className={faClass} />&nbsp;{title}</a>&nbsp;{type}
                </td>
            </tr>
        )
    }
}


export default class ContactContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
        };

    }

    async componentWillMount() {
        this.setState({data: await getData(getUrl('me'))});
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

                        <div className={this.props.width < this.props.responsiveBreakpoint ? "col-xl" : "col-md-6"}>
                            <div className="card border-secondary mb-2">
                                <div className="card-body">
                                    <h4 className="card-title">{this.state.stateRouteName}</h4>
                                    <table className="table">
                                        <thead>
                                        </thead>
                                        <tbody>
                                        {this.state.data.emails ? this.state.data.emails.map((value, key) => {
                                            return (<TableRow key={key} value={value} type='email'/>)
                                        }) : ''}
                                        {this.state.data.external_links ? this.state.data.phone_numbers.map((value, key) => {
                                            return (<TableRow key={key} value={value} type='phone'/>)
                                        }) : ''}
                                        {this.state.data.external_links ? this.state.data.external_links.map((value, key) => {
                                            return (<TableRow key={key} value={value}/>)
                                        }) : ''}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>

                        <div className={this.props.width < this.props.responsiveBreakpoint ? "col-xl" : "col-md-6"}>
                            <div className="card border-secondary mb-2">
                                <div className="card-body">
                                    <h4 className="card-title">CV Tech Info</h4>
                                    <table className="table">
                                        <thead>
                                        </thead>
                                        <tbody>
                                        <tr>
                                            <td>Backend</td>
                                            <td>
                                                <a href="https://www.djangoproject.com/">Django 2</a><br />
                                                <a href="https://www.django-rest-framework.org/">Django REST Framework</a>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>Frontend</td>
                                            <td><a href="https://reactjs.org/">ReactJS</a></td>
                                        </tr>
                                        <tr>
                                            <td>UI Kit</td>
                                            <td><a href="http://getbootstrap.com/">Bootstrap 4</a></td>
                                        </tr>
                                        <tr>
                                            <td>UI Theme</td>
                                            <td>Yeti from <a href="https://bootswatch.com/yeti/">BootSwatch</a></td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>

                        <div className="col-sm">
                        </div>
                    </div>
                </div>
            </div>
        )
    }

}
