run-agent:
	PYTHONPATH=src python3 src/run_agent.py

run-streamlit:
	PYTHONPATH=src streamlit run src/streamlit_app.py