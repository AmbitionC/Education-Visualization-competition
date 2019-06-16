import React from 'react';
import { OverlayTrigger , Tooltip } from 'react-bootstrap';

function SubIcon(props) {
    const span = <span className='teacher'>{props.sub}</span>;
    return (
        <OverlayTrigger
            key={'bottom'}
            placement={'bottom'}
            overlay={
                <Tooltip bsPrefix='tooltip-0'>
                    <span style={{color: '#7189aa'}}>{props.teacher}</span>
                </Tooltip>
            }
        >
            {span}
        </OverlayTrigger>
    );
}

export default function() {
    return (
        <React.Fragment>
            <SubIcon sub={'语'} teacher={'No.53 唐老师'} />
            <SubIcon sub={'数'} teacher={'No.316 鲁老师'} />
            <SubIcon sub={'英'} teacher={'No.26 程老师'} />
            {/* <SubIcon sub={'理'} teacher={'王老师'} /> */}
            {/* <SubIcon sub={'化'} teacher={'王老师'} /> */}
            {/* <SubIcon sub={'生'} teacher={'王老师'} /> */}
            {/* <SubIcon sub={'政'} teacher={'王老师'} /> */}
            {/* <SubIcon sub={'史'} teacher={'王老师'} /> */}
            {/* <SubIcon sub={'地'} teacher={'王老师'} /> */}
            <SubIcon sub={'技'} teacher={'No.158 俞老师'} />
            <SubIcon sub={'体'} teacher={'No.262 效老师'} />
            <SubIcon sub={'美'} teacher={'No.213 程老师'} />
            <SubIcon sub={'音'} teacher={'No.312 过老师'} />
        </React.Fragment>
    );
}