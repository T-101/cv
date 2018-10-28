import React from "react";

class DataListItem extends React.Component {
    render() {
        return (
            <li className="no-list-style">{this.props.item.name}</li>
        )
    }
}

class DataList extends React.Component {
    render() {

        return (
            <div>
                <h6 className="card-subtitle text-muted">
                    {this.props.list.date_start} - {this.props.list.date_end}
                    {this.props.list.employment_status ? ' (' + this.props.list.employment_status + ')' : ''}
                    </h6>
                <div className="card-text text-muted">
                    <ul>
                        {this.props.list.employment_tasks.map((item, i) => {
                            return (<DataListItem key={i} item={item}/>)
                        })}
                    </ul>
                </div>
            </div>
        )
    }
}


export default class DataRow extends React.Component {
    render() {

        function HeaderLine(type, item) {
            if (item && type === "header") {
                return (<h5 className="card-title">{item.name}</h5>)
            } else if (item && type === "subheader") {
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

                {this.props.dataitem.employments ? this.props.dataitem.employments.map((list, l) => {
                    return (<DataList key={l} list={list}/>)
                }) : null}
            </div>
        )
    }
}
