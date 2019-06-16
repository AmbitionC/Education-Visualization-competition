import React from 'react';
import { OverlayTrigger , Popover } from 'react-bootstrap';

export default function (props) {
    const popover = (
        <Popover>
            {
                props.content.map((items, index) => {
                    const span = <span key={index} className='text-muted'>{items}</span>;
                    if (index > 0) {
                        return (
                            <React.Fragment key={index}>
                                <hr />
                                {span}
                            </React.Fragment>
                        );
                    }
                    return span;
                })
            }
        </Popover>
    );
    return (
        <OverlayTrigger trigger="click" placement="left" overlay={popover}>
            <button className="badge badge-info border-0 ml-2">{'说明'}</button>
        </OverlayTrigger>
    );
}