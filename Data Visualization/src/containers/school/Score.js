import React from 'react';
import Score1 from '../../components/SchoolScore1';
import Score2 from '../../components/SchoolScore2';
import Score3 from '../../components/SchoolScore3';
import Score4 from '../../components/SchoolScore4';
import Score5 from '../../components/SchoolScore5';
import Score6 from '../../components/SchoolScore6';

export default function() {
    return (
        <React.Fragment>
            <div className='row mb-3'>
                <div className='col-12 col-lg-6'>
                    <Score5 />
                </div>
                <div className='col-12 col-lg-6'>
                    <Score6 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-lg'>
                    <Score1 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-6'>
                    <Score2 />
                </div>
                <div className='col-12 col-lg-6'>
                    <Score4 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-lg'>
                    <Score3 />
                </div>
            </div>
        </React.Fragment>
    );
}