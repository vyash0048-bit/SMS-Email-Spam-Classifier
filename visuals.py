# Visual component drawings for the Streamlit Spam Classifier
# ALL HTML strings are compressed into single-line formats to prevent Streamlit Markdown indent-parsing bugs.

def draw_probability_gauge(probability):
    """
    Renders a custom animated SVG gauge reflecting the spam probability with glow effects.
    """
    percentage = round(probability * 100, 1)
    # Circumference for r=80 is 2 * pi * 80 ≈ 502.6
    stroke_offset = 502.6 - (502.6 * probability)
    
    if probability >= 0.7:
        color_start = "#f87171"
        color_end = "#ef4444"
        glow_color = "rgba(239, 68, 68, 0.4)"
        status_label = "CRITICAL SPAM"
    elif probability >= 0.3:
        color_start = "#fbbf24"
        color_end = "#f59e0b"
        glow_color = "rgba(245, 158, 11, 0.4)"
        status_label = "SUSPICIOUS"
    else:
        color_start = "#34d399"
        color_end = "#10b981"
        glow_color = "rgba(16, 185, 129, 0.4)"
        status_label = "SAFE (HAM)"

    html_code = f'<div style="position: relative; width: 220px; height: 220px; margin: 0 auto; display: flex; justify-content: center; align-items: center;"><svg width="220" height="220" viewBox="0 0 200 200" style="transform: rotate(-90deg); filter: drop-shadow(0 0 10px {glow_color});"><defs><linearGradient id="gaugeGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{color_start}" /><stop offset="100%" stop-color="{color_end}" /></linearGradient></defs><circle cx="100" cy="100" r="80" stroke="rgba(255, 255, 255, 0.05)" stroke-width="12" fill="transparent" /><circle cx="100" cy="100" r="80" stroke="url(#gaugeGrad)" stroke-width="12" fill="transparent" stroke-dasharray="502.6" stroke-dashoffset="{stroke_offset}" stroke-linecap="round" style="transition: stroke-dashoffset 1s ease-in-out; animation: fillRing 1.2s cubic-bezier(0.4, 0, 0.2, 1) forwards;" /></svg><div style="position: absolute; text-align: center; font-family: \'Plus Jakarta Sans\', sans-serif;"><div style="font-size: 32px; font-weight: 800; color: #ffffff; line-height: 1;">{percentage}%</div><div style="font-size: 9px; font-weight: 700; color: #94a3b8; letter-spacing: 0.12em; text-transform: uppercase; margin-top: 6px;">{status_label}</div></div></div>'
    return html_code


def draw_result_banner(result_cat):
    """
    Renders styled glass banners indicating threat levels.
    """
    if result_cat == "SPAM":
        return '<div class="res-container" style="margin-top: 20px;"><div class="res-banner spam"><h4 style="color: #f87171; font-weight: 800; margin-bottom: 6px; font-size: 16px;">⚠️ Threat Verified</h4><p style="color: #cbd5e1; font-size: 13px; margin: 0; line-height: 1.4;">High confidence spam. Refrain from following any instructions, calling support lines, or clicking links.</p></div></div>'
    elif result_cat == "SUSPICIOUS":
        return '<div class="res-container" style="margin-top: 20px;"><div class="res-banner suspicious"><h4 style="color: #fbbf24; font-weight: 800; margin-bottom: 6px; font-size: 16px;">⚡ Suspicious Markers</h4><p style="color: #cbd5e1; font-size: 13px; margin: 0; line-height: 1.4;">Moderate risk patterns detected. Exercise caution and verify sender identity independently.</p></div></div>'
    else:
        return '<div class="res-container" style="margin-top: 20px;"><div class="res-banner ham"><h4 style="color: #34d399; font-weight: 800; margin-bottom: 6px; font-size: 16px;">🛡️ Safe Verification</h4><p style="color: #cbd5e1; font-size: 13px; margin: 0; line-height: 1.4;">This message shows normal communication habits. No threat indicators were recognized.</p></div></div>'


def draw_sidebar_header():
    """
    Renders the sidebar threat header.
    """
    return '<div style="text-align: center; padding: 20px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 20px;"><span style="font-size: 40px;">🛡️</span><h2 style="color: #ffffff; font-weight: 800; font-size: 22px; margin-top: 10px; margin-bottom: 2px;">SentinShield</h2><span style="color: #6366f1; font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em;">AI Threat Intelligence</span></div>'


def draw_history_item(item, tag_class):
    """
    Renders session log history items inside the sidebar.
    """
    return f'<div class="hist-item"><span class="hist-tag {tag_class}">{item["result"]}</span><div style="color: #e2e8f0; font-weight: 500; font-size: 12px; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">"{item["text"]}"</div><div style="color: #64748b; font-size: 11px;">Confidence: {round(item["proba"]*100, 1)}%</div></div>'


def draw_hero_section():
    """
    Renders the main top header hero banner.
    """
    return '<div class="hero-container"><h1 class="hero-title">Email & SMS Spam Classifier</h1><p class="hero-subtitle">Protect your inbox with real-time, state-of-the-art NLP threat detection. Filter out credential harvesting, smishing, and spam patterns instantly.</p></div>'


def draw_stats_grid(chars, words, read_time):
    """
    Renders the live text stats grid inside a fully closed glass-card.
    """
    return f'<div class="glass-card"><div class="stats-grid"><div class="stats-card"><div class="value">{chars}</div><div class="label">Characters</div></div><div class="stats-card"><div class="value">{words}</div><div class="label">Words</div></div><div class="stats-card"><div class="value">{read_time}s</div><div class="label">Est. Read Time</div></div></div></div>'


def draw_diagnostics_grid(metrics):
    """
    Renders the model diagnostics KPI stats inside a beautiful, fully closed glass-card.
    """
    return f'<div class="glass-card"><div class="diag-grid"><div class="diag-card accuracy"><div class="diag-val">{round(metrics["accuracy"] * 100, 2)}%</div><div class="diag-lbl">General Accuracy</div></div><div class="diag-card precision"><div class="diag-val">{round(metrics["precision"] * 100, 2)}%</div><div class="diag-lbl">Precision (No False Alarms)</div></div><div class="diag-card recall"><div class="diag-val">{round(metrics["recall"] * 100, 2)}%</div><div class="diag-lbl">Recall (Spam Caught)</div></div><div class="diag-card f1"><div class="diag-val">{round(metrics["f1_score"] * 100, 2)}%</div><div class="diag-lbl">F1 Stability Score</div></div></div></div>'


def draw_confusion_matrix(cm):
    """
    Renders the confusion matrix inside a beautiful, fully closed glass-card.
    """
    return f'<div class="glass-card"><h3 style="color:#ffffff; font-weight:700; margin-bottom:15px; font-size: 18px;">📊 Confusion Matrix Layout</h3><table class="cm-table"><tr><td class="cm-cell cm-header" style="width:20%">Actual \\ Predicted</td><td class="cm-cell cm-header" style="width:40%">Predicted Ham (Safe)</td><td class="cm-cell cm-header" style="width:40%">Predicted Spam (Danger)</td></tr><tr><td class="cm-cell label-col">Actual Ham (Safe)</td><td class="cm-cell value tn">{cm[0][0]}<br/><span style="font-size:10px; font-weight:500; opacity: 0.8;">True Negatives (Correctly Cleared)</span></td><td class="cm-cell value fp">{cm[0][1]}<br/><span style="font-size:10px; font-weight:500; opacity: 0.8;">False Positives (Incorrect Flag)</span></td></tr><tr><td class="cm-cell label-col">Actual Spam (Danger)</td><td class="cm-cell value fn">{cm[1][0]}<br/><span style="font-size:10px; font-weight:500; opacity: 0.8;">False Negatives (Missed Threats)</span></td><td class="cm-cell value tp">{cm[1][1]}<br/><span style="font-size:10px; font-weight:500; opacity: 0.8;">True Positives (Threats Verified)</span></td></tr></table></div>'


def draw_diagnostics_insight(metrics, cm):
    """
    Renders the deep-dive analysis guidelines callout box.
    """
    return f'<div style="margin-top: 15px; font-size: 13.5px; color: #94a3b8; line-height:1.6; padding: 15px; background: rgba(99, 102, 241, 0.05); border-radius: 10px; border: 1px solid rgba(99, 102, 241, 0.15);">💡 <strong>Security Deep Dive:</strong> With a Precision of <strong>{round(metrics["precision"] * 100, 1)}%</strong>, the classifier records <strong>exactly {cm[0][1]} False Positives</strong> out of {cm[0][0] + cm[0][1]} test cases. This ensures that valid communications (billing statements, work emails) are never blocked mistakenly, retaining maximum transactional integrity while the high accuracy rate ({round(metrics["accuracy"] * 100, 1)}%) keeps your inbox clean from malicious threat scripts.</div>'


def draw_shield_guidelines():
    """
    Renders the Safe-Inbox Protection Guidelines dashboard card.
    """
    return '<div class="glass-card"><h3 style="color: #6366f1; font-weight: 800; margin-bottom: 20px; font-size: 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding-bottom: 10px;">🛡️ Safe-Inbox Protection Guidelines</h3><div style="margin-bottom: 25px;"><h4 style="color: #f1f5f9; font-weight: 700; font-size: 16px; margin-bottom: 8px;">1. Pay Close Attention to Urgency</h4><p style="color: #94a3b8; font-size: 14px; line-height: 1.6; margin: 0;">Spammers and phishers rely on artificial emotional triggers like panic or fear (e.g., <em>"ACT IMMEDIATELY"</em>, <em>"Account suspended in 2 hours"</em>) to bypass your rational review. If an email or SMS demands swift, immediate action regarding account security or finances, slow down and investigate directly.</p></div><div style="margin-bottom: 25px;"><h4 style="color: #f1f5f9; font-weight: 700; font-size: 16px; margin-bottom: 8px;">2. Watch out for Spoofed Domain Links</h4><p style="color: #94a3b8; font-size: 14px; line-height: 1.6; margin: 0;">Before touching or clicking hyperlinks inside incoming communications, check the domain carefully. Watch for small typographical shifts (e.g. <code>secure-netf1ix.com</code> instead of <code>netflix.com</code>). Malicious URLs represent the primary delivery mechanism for corporate credential harvesting.</p></div><div style="margin-bottom: 10px;"><h4 style="color: #f1f5f9; font-weight: 700; font-size: 16px; margin-bottom: 8px;">3. Never Share MFA / One-Time Passwords</h4><p style="color: #94a3b8; font-size: 14px; line-height: 1.6; margin: 0;">Security support teams and institutions will never ask you to read back or enter a multi-factor authorization code or OTP over SMS/Email. Treat authentication codes as highly confidential keys that are private to you alone.</p></div></div>'


def draw_idle_standby():
    """
    Renders the standby card waiting for user input.
    """
    return '<div class="glass-card" style="text-align: center; padding: 40px 20px;"><div style="font-size: 48px; margin-bottom: 15px; opacity: 0.6;">⏳</div><h3 style="color:#ffffff; font-weight:700; margin-bottom:10px; font-size: 17px;">Awaiting Message Input</h3><p style="color:#64748b; font-size: 13px; line-height:1.5;">Provide a message in the input field and click the scan button to view real-time confidence scores and analytical reports.</p></div>'
