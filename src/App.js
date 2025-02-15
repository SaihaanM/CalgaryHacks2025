import React from 'react';
import { FilterProvider } from './context/FilterContext';
import DealsList from './components/DealsList';
import FilterPanel from './components/FilterPanel';
import './styles/popup.css';

function App() {
  return (
    <FilterProvider>
      <div className="app-container">
        <h1>Better Deal Finder</h1>
        <FilterPanel />
        <DealsList />
      </div>
    </FilterProvider>
  );
}

export default App; 