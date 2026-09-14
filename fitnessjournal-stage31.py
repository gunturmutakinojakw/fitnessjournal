# === Stage 31: Add compact table rendering for long lists ===
# Project: FitnessJournal
def render_compact_table(headers, rows):
    """Render long lists as a compact HTML table with scrollable container."""
    width = "100%"
    style = f"width:{width};overflow:auto;font-family:monospace;font-size:12px;"
    html = f'<div style="{style}"><table><thead><tr>'
    for h in headers:
        html += f"<th style='padding:2px 4px;white-space:nowrap;'>{h}</th>"
    html += "</tr></thead><tbody>"
    for row in rows:
        html += "<tr>"
        for cell in row:
            html += f"<td style='padding:2px 4px;'>{cell}</td>"
        html += "</tr>"
    html += "</tbody></table></div>"
    return html
