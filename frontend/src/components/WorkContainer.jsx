import React from 'react'
import {Card} from "react-bootstrap";
import {DataContext} from "../contexts/DataContext";

export default function LandingPageContainer() {
    const {data} = React.useContext(DataContext)
    return (
        <Card style={{marginTop: "30px"}}>
            <Card.Header>Work</Card.Header>
            <Card.Body>
                {data && data.employers.map((employer, key) => (
                        <span key={key}>
                            {key !== 0 && <hr />}
                            <Card.Title>
                                <strong>{employer.name}</strong>
                                {employer.url &&
                                <a href={employer.url} style={{marginLeft: "1rem"}}><i className="fas fa-external-link-alt" /></a>
                                }
                            </Card.Title>
                            <Card.Subtitle className="text-muted"><span>{employer.description}</span></Card.Subtitle>
                            {employer.employments.map((employment, itemKey) => (
                                <span key={itemKey}>
                                    <br />
                                    <Card.Subtitle className="text-muted">
                                        {employment.title && <span>
                                            <span style={{color: "#000000"}}>{employment.title}</span>
                                            {employment.employment_status && <i>{" (" + employment.employment_status + ")"}</i>}
                                            <br/>
                                        </span>}
                                        {employment.date_start} - {employment.date_end && employment.date_end}
                                    </Card.Subtitle>
                                    <ul style={{listStyleType: "square"}}>
                                        {employment.employment_tasks.map((task, taskKey) => (
                                            <li key={taskKey}>{task.name}</li>
                                        ))}
                                    </ul>
                                </span>
                            ))}
                        </span>
                    )
                )}
            </Card.Body>
        </Card>
    )
}
