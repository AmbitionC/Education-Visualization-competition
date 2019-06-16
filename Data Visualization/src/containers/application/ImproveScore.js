import React from 'react';
import ImporveScore1 from '../../components/ApplicationImproveScore1.js'
import ImporveScore2 from '../../components/ApplicationImproveScore2.js'
import ImporveScore3 from '../../components/ApplicationImproveScore3.js'

export default function(){
    return (
        <React.Fragment>
            <div className='row mb-3'>
                <div className='col'>
                    <ImporveScore1 />                 
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <ImporveScore2 />                 
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <ImporveScore3 />
                </div>
            </div>
        </React.Fragment>
    )
}