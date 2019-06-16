import React from 'react';
import Teacher1 from '../../components/SchoolTeacher1';
import Teacher2 from '../../components/SchoolTeacher2';
import Teacher3 from '../../components/SchoolTeacher3';

export default function() {
    return (
        <React.Fragment>
            <div className='row mb-3'>
                <div className='col-12 col-lg-4'>
                        <Teacher1 />
                </div>
                <div className='col-12 col-lg-8'>
                        <Teacher2 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col'>
                    <Teacher3 />
                </div>
            </div>
        </React.Fragment>
    );
}
