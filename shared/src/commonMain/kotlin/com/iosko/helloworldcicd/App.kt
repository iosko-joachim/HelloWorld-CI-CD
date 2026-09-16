package com.iosko.helloworldcicd

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier

// S-001 Hello-World-Screen (projekt/ui/S-001.md): zeigt nur diesen Text.
private const val GREETING = "Здравей, свят!"

@Composable
fun App() {
    MaterialTheme {
        Surface {
            Box(
                modifier = Modifier.fillMaxSize(),
                contentAlignment = Alignment.Center
            ) {
                Text(GREETING)
            }
        }
    }
}
