import React from 'react';
import ThreeInSeven1 from '../../components/Application3In71.js'
import ThreeInSeven2 from '../../components/Application3In72.js'
import ThreeInSeven3 from '../../components/Application3In73.js'
import ThreeInSeven4 from '../../components/Application3In74.js'

export default function(){
    return (
        <React.Fragment>
            <div className='row mb-3'>
                <div className='col'>
                    <ThreeInSeven3 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-3'>
                    <ThreeInSeven1 />
                </div>
                <div className='col-12 col-lg-9'>
                    <ThreeInSeven2 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-12'>
                    <ThreeInSeven4 />
                </div>
            </div>
        </React.Fragment>
    )
}