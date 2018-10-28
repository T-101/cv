import React from "react";
import '../bootswatch.yeti.min.css';
import Link from "react-router-dom/es/Link";

export default class PartyTableContainer extends React.Component {


    render() {
        return (
            <div className={this.props.width < this.props.responsiveBreakpoint ? "" : "top-flat"}>
                <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
                    <Link to={this.props.routes.welcome.url} className="navbar-brand">{this.props.realname}</Link>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01"
                            aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>

                    <div className="collapse navbar-collapse" id="navbarColor01">
                        <ul className="navbar-nav mr-auto">
                            <li className={this.props.match.url === this.props.routes.welcome.url ? "nav-item active" : "nav-item"}>
                                <Link className="nav-link"
                                      to={this.props.routes.welcome.url}>{this.props.routes.welcome.name}</Link>
                            </li>
                            <li className={this.props.match.url === this.props.routes.me.url ? "nav-item active" : "nav-item"}>
                                <Link className="nav-link"
                                      to={this.props.routes.me.url}>{this.props.routes.me.name}</Link>
                            </li>
                            <li className={this.props.match.url === this.props.routes.work.url ? "nav-item active" : "nav-item"}>
                                <Link className="nav-link"
                                      to={this.props.routes.work.url}>{this.props.routes.work.name}</Link>
                            </li>
                            <li className={this.props.match.url === this.props.routes.hobby.url ? "nav-item active" : "nav-item"}>
                                <Link className="nav-link"
                                      to={this.props.routes.hobby.url}>{this.props.routes.hobby.name}</Link>
                            </li>
                            <li className={this.props.match.url === this.props.routes.contact.url ? "nav-item active" : "nav-item"}>
                                <Link className="nav-link"
                                      to={this.props.routes.contact.url}>{this.props.routes.contact.name}</Link>
                            </li>
                        </ul>
                    </div>
                </nav>
            </div>
        )
    }

}
