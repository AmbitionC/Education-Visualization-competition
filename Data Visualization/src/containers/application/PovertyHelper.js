import React from 'react';
import PovertyHelper1 from '../../components/ApplicationPoverty1.js'
import PovertyHelper2 from '../../components/ApplicationPoverty2.js'
import PovertyHelper3 from '../../components/ApplicationPoverty3.js'
import PovertyHelper5 from '../../components/ApplicationPoverty5.js'

export default function() {
    return (
        <React.Fragment>
            <div className='row mb-3'>
                <div className='col'>
                    <PovertyHelper1 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <PovertyHelper2 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <PovertyHelper3 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <PovertyHelper5 />
                </div>
            </div>
        </React.Fragment>
    )
}