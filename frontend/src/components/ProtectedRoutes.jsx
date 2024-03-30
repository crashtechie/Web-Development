import {Navigate} from 'react-router-dom';
import {jwtDecode} from 'jwt-decode';
import api from '../api';
import {REFRESH_TOKEN,ACCESS_TOKEN} from '../constants';
import {useEffect, useState} from 'react';

function ProtectedRoute({children}) {
    const [isAuthenticated, setIsAuthenticated] = useState(null);

    useEffect(() => {
        auth().catch(() => { isAuthenticated(false); });
    }, []);

    const refreshToken = async () => {
        const refreshtoken = localStorage.getItem(REFRESH_TOKEN);
        if (!refreshtoken) {
            Navigate('/login');
        }
        try {
            const response = await api.post('/api/token/refresh/', {refresh: refreshtoken});
            if (response.status == 200) {
                localStorage.setItem(ACCESS_TOKEN, response.data.access);
                setIsAuthenticated(true);
            } else {
                setIsAuthenticated(false);
                Navigate('/login');
            }
        } catch (error) {
            console.error(error);
            setIsAuthenticated(false);
            Navigate('/login');
        }
    }

    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (!token) {
            setIsAuthenticated(false);
            Navigate('/login');
            return;
        }
        try {
            const data = jwtDecode(token);
            if (data.exp * 1000 < Date.now()) {
                await refreshToken();
            } else {
                setIsAuthenticated(true);
            }
        } catch (error) {
            console.error(error);
            Navigate('/login');
        }
    }

    if (!isAuthenticated) {
        return <div><h1>Loading...</h1></div>;
    }

    return isAuthenticated ? children : <Navigate to='/login' />;
}

export default ProtectedRoute;