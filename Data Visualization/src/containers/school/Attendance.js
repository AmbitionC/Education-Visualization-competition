import React from 'react';
import Attend1 from '../../components/SchoolAttendance1.js'
import Attend2 from '../../components/SchoolAttendance2.js'
import Attend3 from '../../components/SchoolAttendance3.js'
import Attend4 from '../../components/SchoolAttendance4.js'
import Attend5 from '../../components/SchoolAttendance5.js'
import Attend6 from '../../components/SchoolAttendance6.js'

export default function(){
    return (
        <React.Fragment>
            <div className='row mb-3'>
                <div className='col-12 col-lg-4'>
                    <Attend2/>
                </div>
                <div className='col-12 col-lg-4'>
                    <Attend3/>
                </div>
                <div className='col-12 col-lg-4'>
                    <Attend4/>
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <Attend5/>
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <Attend6/>
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <Attend1/>
                </div>
            </div>
        </React.Fragment>
    )
}