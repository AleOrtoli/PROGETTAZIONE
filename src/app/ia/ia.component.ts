import { Component, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';

interface Message {
  type: 'domanda' | 'risposta';
  text: string;
}

@Component({
  standalone: true,
  selector: 'app-ia',
  templateUrl: './ia.component.html',
  styleUrl: './ia.component.css',
  imports: [CommonModule] 
  
})
export class IaComponent {
  @ViewChild('domanda') domandaInput!: ElementRef;
  messages: Message[] = [];
  


  constructor(private http: HttpClient) { }

  submit(): void {
    const domanda = this.domandaInput.nativeElement.value;
    if (!domanda) {
      alert('Per favore, inserisci una domanda.');
      return;
    }
  
    // Aggiungi la domanda alla lista dei messaggi
    this.messages.push({ type: 'domanda', text: domanda});
    // Resetta il campo di input
    this.domandaInput.nativeElement.value = '';

    // Invia la domanda al server
    this.http.post<any>('http://localhost:3000', { domanda }).subscribe({
      next: (response) => {
        // Ricevi la risposta dal server
        const rispostaTesto = response; // Estrai il testo dalla risposta JSON
        this.messages.push({ type: 'risposta', text: rispostaTesto });
        
      },
      error: (error) => {
        console.error('Si è verificato un errore durante l\'invio della domanda:', error);
      }
    });
    // Resetta il campo di input
    this.domandaInput.nativeElement.value = '';
  }
}
