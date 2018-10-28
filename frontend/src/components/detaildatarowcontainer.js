import React from "react";


class DetailItem extends React.Component {
    render() {

        return (
            <div className="card-text text-muted">
                <li className="no-list-style">{this.props.list.text}</li>
            </div>
        )
    }
}


export default class DetailDataRow extends React.Component {
    render() {

        function HeaderLine(type, item) {
            if (item && type === "header") {
                return (<h5 className="card-title">{item.name}</h5>)
            } else if (item && type === "subheader" && item.description) {
                return (
                    <div>
                        <h6 className="card-subtitle text-muted">{item.description}</h6>
                        <br/>
                    </div>
                )
            }
        }

        return (
            <div className="card-body">
                {HeaderLine("header", this.props.dataitem)}
                {HeaderLine("subheader", this.props.dataitem)}
                <ul>
                    {this.props.dataitem.items ? this.props.dataitem.items.map((list, l) => {
                        return (<DetailItem key={l} list={list}/>)
                    }) : null}
                </ul>

            </div>
        )
    }
}
