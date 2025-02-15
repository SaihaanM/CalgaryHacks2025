const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const searchDeals = async (productInfo) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/search`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(productInfo)
    });
    return await response.json();
  } catch (error) {
    console.error('Error searching deals:', error);
    throw error;
  }
}; 