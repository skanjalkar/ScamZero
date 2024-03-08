package com.example.callfowarding

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.telephony.TelephonyManager

class CallStateReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == TelephonyManager.ACTION_PHONE_STATE_CHANGED) {
            val state = intent.getStringExtra(TelephonyManager.EXTRA_STATE)
            when (state) {
                TelephonyManager.EXTRA_STATE_RINGING -> {
                    // The phone is ringing
                }
                TelephonyManager.EXTRA_STATE_OFFHOOK -> {
                    // A call is dialing, active or on hold
                }
                TelephonyManager.EXTRA_STATE_IDLE -> {
                    // The phone is neither ringing nor in a call
                }
            }
        }
    }
}