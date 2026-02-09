# Configure rate limiting per site if needed
site_configs = {
    "Amar Desh": {
        "max_workers": 5,
        "delay": 1.5,  # API endpoint, can be faster
        "timeout": 15,  # Added timeout parameter
    },
    "Prothom Alo": {
        "max_workers": 3,  # Conservative - major site with protection
        "delay": 2.5,
        "timeout": 20,
        "retries": 2,  # Add retry for robustness
    },
    "Kaler Kantho": {
        "max_workers": 4, 
        "delay": 2.0, 
        "timeout": 25
    },
    "Daily Noya Diganta": {
        "max_workers": 3,  # HTML parsing might be slower
        "delay": 2.0,
        "timeout": 15,
    },
    "Jugantor": {
        "max_workers": 2,  # Very conservative - AJAX endpoint
        "delay": 3.0,  # Longer delay for safety
        "timeout": 20,
        "retries": 3,
    },
    "Daily Sangram": {
        "max_workers": 3, 
        "delay": 2.0, 
        "timeout": 20
    },
    "Bonik Bartha (Bangla)": {
        "max_workers": 3, 
        "delay": 2.0, 
        "timeout": 15
    },
    "Bonik Bartha (English)": {
        "max_workers": 3, 
        "delay": 2.0, 
        "timeout": 15
    },
    "The Business Standard (Bangla)": {
        "max_workers": 3, 
        "delay": 2.0, 
        "timeout": 15
    },
    "The Business Standard (English)": {
        "max_workers": 3, 
        "delay": 2.0, 
        "timeout": 15
    },
    "The Daily Star": {
        "max_workers": 3, 
        "delay": 2.0, 
        "timeout": 15
    }, 
    "The Financial Times": {
        "max_workers": 3,  # Conservative - major site with protection
        "delay": 2.5,
        "timeout": 20,
        "retries": 2,
    },
    "The Daily Observer": {
        "max_workers": 3,  # HTML parsing might be slower
        "delay": 2.5,
        "timeout": 30,
    },
    "Ars Technica": {
        "max_workers": 3,  # HTML parsing might be slower
        "delay": 2.0,
        "timeout": 15,
    },
    "Bangladesh Pratidin": {
        "max_workers": 3,  # HTML parsing might be slower
        "delay": 2.0,
        "timeout": 15,
    },
    "Dhaka Tribune": {
        "max_workers": 3,  # HTML parsing might be slower
        "delay": 2.0,
        "timeout": 15,
    },
    "The Daily Inquilab": {
        "max_workers": 3,  # HTML parsing might be slower
        "delay": 2.0,
        "timeout": 15,
    },
    "Wired": {
        "max_workers": 3,  # HTML parsing might be slower
        "delay": 2.0,
        "timeout": 15,
    }
}
